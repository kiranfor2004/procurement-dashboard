# app.py - Procurement Dashboard Backend
import pandas as pd
import numpy as np
from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os
from datetime import datetime

# Create Flask app
app = Flask(__name__)
CORS(app)

print("🚀 Starting Procurement Dashboard...")

# Try to load data file
try:
    if os.path.exists('Purchase data.csv'):
        df = pd.read_csv('Purchase data.csv')
        print(f"✅ Loaded {len(df)} records from Purchase data.csv")
    else:
        print("⚠️  Purchase data.csv not found. Creating sample data...")
        # Create minimal sample data
        sample_data = {
            'TOTAL AMOUNT': ['$1000.00', '$2000.00', '$500.00'],
            'VENDOR NAME 1': ['Sample Vendor A', 'Sample Vendor B', 'Sample Vendor C'],
            'DEPARTMENT NAME': ['Finance', 'IT', 'HR'],
            'INPUT DATE': ['08/01/2025', '08/15/2025', '08/28/2025'],
            'MINORITY': ['Y', 'N', 'Y'],
            'SB WOMAN': ['N', 'Y', 'N'],
            'SB VETERAN': ['N', 'N', 'Y'],
            'DOCUMENT STATUS DESCRIPTION': ['Posted', 'Posted', 'Posted']
        }
        df = pd.DataFrame(sample_data)
        print("🔄 Using sample data for demonstration")
    
    # Clean money amounts
    def clean_money(amount_str):
        if pd.isna(amount_str):
            return 0
        try:
            return float(str(amount_str).replace('$', '').replace(',', ''))
        except:
            return 0
    
    # Clean data
    df['total_amount_clean'] = df['TOTAL AMOUNT'].apply(clean_money)
    
    # Convert dates
    df['input_date'] = pd.to_datetime(df['INPUT DATE'], errors='coerce')
    df['year'] = df['input_date'].dt.year
    df['month'] = df['input_date'].dt.month
    
    # Calculate basic stats
    total_spend = df['total_amount_clean'].sum()
    total_transactions = len(df)
    avg_transaction = total_spend / total_transactions if total_transactions > 0 else 0
    unique_vendors = df['VENDOR NAME 1'].nunique()
    
    print(f"📊 Stats: ${total_spend:,.2f} total, {total_transactions} transactions, {unique_vendors} vendors")
    
except Exception as e:
    print(f"❌ Error loading data: {e}")
    df = pd.DataFrame()  # Empty dataframe

# API Routes
@app.route('/')
def home():
    return """
    <h1>🎉 Procurement Dashboard API</h1>
    <p>✅ Backend is running!</p>
    <p><a href="/api/summary">View Summary Data</a></p>
    <p>Open dashboard.html in your browser to see the full dashboard!</p>
    """

@app.route('/api/summary')
def get_summary():
    try:
        if df.empty:
            return jsonify({'error': 'No data available'})
        
        # Diversity metrics
        minority_spend = df[df['MINORITY'] == 'Y']['total_amount_clean'].sum()
        woman_spend = df[df['SB WOMAN'] == 'Y']['total_amount_clean'].sum()
        veteran_spend = df[df['SB VETERAN'] == 'Y']['total_amount_clean'].sum()
        
        minority_pct = (minority_spend / total_spend * 100) if total_spend > 0 else 0
        woman_pct = (woman_spend / total_spend * 100) if total_spend > 0 else 0
        veteran_pct = (veteran_spend / total_spend * 100) if total_spend > 0 else 0
        
        # Top vendors
        top_vendors = df.groupby('VENDOR NAME 1')['total_amount_clean'].sum().nlargest(5)
        top_5_spend = top_vendors.sum()
        vendor_concentration = (top_5_spend / total_spend * 100) if total_spend > 0 else 0
        
        return jsonify({
            'total_spend': total_spend,
            'total_transactions': total_transactions,
            'avg_transaction': avg_transaction,
            'unique_vendors': unique_vendors,
            'vendor_concentration': vendor_concentration,
            'diversity': {
                'minority_spend_pct': minority_pct,
                'woman_spend_pct': woman_pct,
                'veteran_spend_pct': veteran_pct
            },
            'top_vendors': top_vendors.to_dict()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/charts/spend_trend')
def get_spend_trend():
    try:
        if df.empty or df['input_date'].isna().all():
            return jsonify({
                'labels': ['2025-01', '2025-02', '2025-03', '2025-04', '2025-05', '2025-06', '2025-07', '2025-08'],
                'values': [1000, 1500, 800, 2000, 1200, 900, 1800, 1600]
            })
        
        monthly_spend = df.groupby(['year', 'month'])['total_amount_clean'].sum().reset_index()
        monthly_spend['date_label'] = (monthly_spend['year'].astype(str) + '-' + 
                                     monthly_spend['month'].astype(str).str.zfill(2))
        monthly_spend = monthly_spend.sort_values(['year', 'month'])
        
        return jsonify({
            'labels': monthly_spend['date_label'].tolist(),
            'values': monthly_spend['total_amount_clean'].tolist()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/charts/top_vendors')
def get_top_vendors():
    try:
        if df.empty:
            return jsonify({
                'labels': ['Sample Vendor A', 'Sample Vendor B', 'Sample Vendor C'],
                'values': [1000, 800, 600]
            })
        
        top_vendors = df.groupby('VENDOR NAME 1')['total_amount_clean'].sum().nlargest(10)
        return jsonify({
            'labels': top_vendors.index.tolist(),
            'values': top_vendors.values.tolist()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/charts/diversity')
def get_diversity_chart():
    try:
        if df.empty:
            return jsonify({
                'labels': ['Minority-Owned', 'Woman-Owned', 'Veteran-Owned', 'Other'],
                'values': [40, 20, 15, 25]
            })
        
        minority_spend = df[df['MINORITY'] == 'Y']['total_amount_clean'].sum()
        woman_spend = df[df['SB WOMAN'] == 'Y']['total_amount_clean'].sum()
        veteran_spend = df[df['SB VETERAN'] == 'Y']['total_amount_clean'].sum()
        other_spend = total_spend - minority_spend - woman_spend - veteran_spend
        other_spend = max(0, other_spend)
        
        total = total_spend if total_spend > 0 else 1
        
        return jsonify({
            'labels': ['Minority-Owned', 'Woman-Owned', 'Veteran-Owned', 'Other'],
            'values': [
                (minority_spend / total) * 100,
                (woman_spend / total) * 100,
                (veteran_spend / total) * 100,
                (other_spend / total) * 100
            ]
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/departments')
def get_departments():
    try:
        if df.empty:
            return jsonify({
                'labels': ['Finance', 'IT', 'HR'],
                'values': [1000, 800, 500]
            })
        
        dept_spend = df.groupby('DEPARTMENT NAME')['total_amount_clean'].sum().sort_values(ascending=False)
        return jsonify({
            'labels': dept_spend.index.tolist(),
            'values': dept_spend.values.tolist()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the app
if __name__ == '__main__':
    print("\n🚀 Flask server starting...")
    print("🌐 API: http://localhost:5000")
    print("📊 Dashboard: Open dashboard.html in browser")
    print("🛑 To stop: Press Ctrl+C")
    print("-" * 50)
    
    app.run(debug=True, port=5001, host='0.0.0.0')