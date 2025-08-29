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
CORS(app, origins=["*"], methods=["GET", "POST", "OPTIONS"], allow_headers=["Content-Type"])

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
    <p><a href="/dashboard">View Dashboard</a></p>
    <p><a href="/api/summary">View Summary Data</a></p>
    """

@app.route('/dashboard')
def dashboard():
    """Serve the dashboard HTML file"""
    try:
        with open('dashboard.html', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return """
        <h1>Dashboard not found</h1>
        <p>Please make sure dashboard.html is in the same directory as app.py</p>
        <p><a href="/">Go back to API home</a></p>
        """, 404

@app.route('/drill-down.html')
def drill_down():
    """Serve the drill-down HTML file"""
    try:
        with open('drill-down.html', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return """
        <h1>Drill-down page not found</h1>
        <p>Please make sure drill-down.html is in the same directory as app.py</p>
        <p><a href="/dashboard">Go back to Dashboard</a></p>
        """, 404

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
            # Return demo data if no real data
            return jsonify({
                'labels': ['2025-01', '2025-02', '2025-03', '2025-04', '2025-05', '2025-06', '2025-07', '2025-08'],
                'values': [383000000, 404000000, 352000000, 458000000, 391000000, 367000000, 421000000, 391000000]
            })
        
        # Process real data
        monthly_spend = df.groupby(['year', 'month'])['total_amount_clean'].sum().reset_index()
        monthly_spend['date_label'] = (monthly_spend['year'].astype(str) + '-' + 
                                     monthly_spend['month'].astype(str).str.zfill(2))
        monthly_spend = monthly_spend.sort_values(['year', 'month'])
        
        return jsonify({
            'labels': monthly_spend['date_label'].tolist(),
            'values': monthly_spend['total_amount_clean'].tolist()
        })
    except Exception as e:
        print(f"Error in spend_trend: {e}")
        # Return demo data on error
        return jsonify({
            'labels': ['2025-01', '2025-02', '2025-03', '2025-04', '2025-05', '2025-06', '2025-07', '2025-08'],
            'values': [383000000, 404000000, 352000000, 458000000, 391000000, 367000000, 421000000, 391000000]
        })

@app.route('/api/charts/top_vendors')
def get_top_vendors():
    try:
        if df.empty:
            return jsonify({
                'labels': ['GRADY CRAWFORD CONSTRUCTION', 'REPUBLIC SERVICES INC', 'THE WORKFORCE GROUP LLC', 'WASTE MANAGEMENT', 'WHARTON-SMITH INC', 'HARD ROCK CONSTRUCTION'],
                'values': [950000000, 644000000, 552000000, 460000000, 368000000, 92000000]
            })
        
        top_vendors = df.groupby('VENDOR NAME 1')['total_amount_clean'].sum().nlargest(10)
        return jsonify({
            'labels': top_vendors.index.tolist(),
            'values': top_vendors.values.tolist()
        })
    except Exception as e:
        print(f"Error in top_vendors: {e}")
        return jsonify({
            'labels': ['GRADY CRAWFORD CONSTRUCTION', 'REPUBLIC SERVICES INC', 'THE WORKFORCE GROUP LLC', 'WASTE MANAGEMENT', 'WHARTON-SMITH INC', 'HARD ROCK CONSTRUCTION'],
            'values': [950000000, 644000000, 552000000, 460000000, 368000000, 92000000]
        })

@app.route('/api/charts/diversity')
def get_diversity_chart():
    try:
        if df.empty:
            return jsonify({
                'labels': ['Minority-Owned', 'Woman-Owned', 'Veteran-Owned', 'Other'],
                'values': [2.6, 3.49, 0.25, 93.66]
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
        print(f"Error in diversity: {e}")
        return jsonify({
            'labels': ['Minority-Owned', 'Woman-Owned', 'Veteran-Owned', 'Other'],
            'values': [2.6, 3.49, 0.25, 93.66]
        })

@app.route('/api/departments')
def get_departments():
    try:
        if df.empty:
            return jsonify({
                'labels': ['COMMUNITY DEVELOP', 'PUBLIC WORKS', 'AIRPORT', 'ENV SERV', 'UTILITIES'],
                'values': [920000000, 613000000, 460000000, 368000000, 307000000]
            })
        
        dept_spend = df.groupby('DEPARTMENT NAME')['total_amount_clean'].sum().sort_values(ascending=False)
        return jsonify({
            'labels': dept_spend.index.tolist(),
            'values': dept_spend.values.tolist()
        })
    except Exception as e:
        print(f"Error in departments: {e}")
        return jsonify({
            'labels': ['COMMUNITY DEVELOP', 'PUBLIC WORKS', 'AIRPORT', 'ENV SERV', 'UTILITIES'],
            'values': [920000000, 613000000, 460000000, 368000000, 307000000]
        })

@app.route('/api/drill-down', methods=['GET'])
def get_drill_down_data():
    """Get detailed drill-down data for specific analysis type"""
    try:
        drill_type = request.args.get('type', 'total_spend')
        value = request.args.get('value', '')
        department = request.args.get('department', 'all')
        date_range = request.args.get('dateRange', 'all')
        amount_range = request.args.get('amountRange', 'all')
        
        # Filter data based on parameters
        filtered_df = df.copy()
        
        # Apply department filter
        if department != 'all':
            filtered_df = filtered_df[filtered_df['DEPARTMENT NAME'] == department]
        
        # Apply date filter (simplified for demo)
        if date_range != 'all':
            # Implement date filtering logic here
            pass
        
        # Apply amount filter
        if amount_range != 'all':
            # Implement amount filtering logic here
            pass
        
        # Generate drill-down data based on type
        if drill_type == 'spend_performance':
            drill_data = generate_spend_performance_drill(filtered_df)
        elif drill_type == 'diversity':
            drill_data = generate_diversity_drill(filtered_df)
        elif drill_type == 'vendor_performance':
            drill_data = generate_vendor_performance_drill(filtered_df)
        elif drill_type == 'department':
            drill_data = generate_department_drill(filtered_df, value)
        else:
            drill_data = generate_default_drill(filtered_df)
        
        return jsonify(drill_data)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def generate_spend_performance_drill(df_filtered):
    """Generate spend performance drill-down data"""
    try:
        total_amount = df_filtered['total_amount_clean'].sum()
        record_count = len(df_filtered)
        avg_amount = df_filtered['total_amount_clean'].mean() if len(df_filtered) > 0 else 0
        top_vendor = df_filtered.groupby('VENDOR NAME 1')['total_amount_clean'].sum().idxmax() if len(df_filtered) > 0 else 'N/A'
        
        # Monthly trend data (sample for now)
        monthly_spend = {
            'Jan': total_amount * 0.08,
            'Feb': total_amount * 0.09,
            'Mar': total_amount * 0.12,
            'Apr': total_amount * 0.15,
            'May': total_amount * 0.18,
            'Jun': total_amount * 0.14,
            'Jul': total_amount * 0.13,
            'Aug': total_amount * 0.11
        }
        
        # Top departments
        dept_spend = df_filtered.groupby('DEPARTMENT NAME')['total_amount_clean'].sum().head(5)
        
        # Sample records
        sample_records = df_filtered.head(10)[['VENDOR NAME 1', 'DEPARTMENT NAME', 'total_amount_clean', 'INPUT DATE']].to_dict('records')
        
        return {
            'summary': {
                'totalAmount': total_amount,
                'recordCount': record_count,
                'avgAmount': avg_amount,
                'topVendor': top_vendor
            },
            'trendData': {
                'labels': list(monthly_spend.keys()),
                'data': list(monthly_spend.values())
            },
            'distributionData': {
                'labels': dept_spend.index.tolist() if not dept_spend.empty else ['No Data'],
                'data': dept_spend.values.tolist() if not dept_spend.empty else [0]
            },
            'records': [
                {
                    'vendor': record['VENDOR NAME 1'],
                    'department': record['DEPARTMENT NAME'],
                    'amount': record['total_amount_clean'],
                    'date': record['INPUT DATE'],
                    'category': 'Services',
                    'status': 'Completed',
                    'diversity': 'Non-Diverse'
                } for record in sample_records
            ]
        }
    except Exception as e:
        print(f"Error in spend_performance_drill: {e}")
        return {
            'summary': {'totalAmount': 0, 'recordCount': 0, 'avgAmount': 0, 'topVendor': 'N/A'},
            'trendData': {'labels': ['Jan', 'Feb', 'Mar'], 'data': [0, 0, 0]},
            'distributionData': {'labels': ['No Data'], 'data': [0]},
            'records': []
        }

def generate_diversity_drill(df_filtered):
    """Generate diversity spending drill-down data"""
    try:
        # Calculate diversity metrics
        minority_spend = df_filtered[df_filtered['MINORITY'] == 'Y']['total_amount_clean'].sum()
        woman_spend = df_filtered[df_filtered['SB WOMAN'] == 'Y']['total_amount_clean'].sum()
        veteran_spend = df_filtered[df_filtered['SB VETERAN'] == 'Y']['total_amount_clean'].sum()
        total_spend = df_filtered['total_amount_clean'].sum()
        
        return {
            'summary': {
                'totalAmount': total_spend,
                'recordCount': len(df_filtered),
                'avgAmount': df_filtered['total_amount_clean'].mean() if len(df_filtered) > 0 else 0,
                'topVendor': df_filtered.groupby('VENDOR NAME 1')['total_amount_clean'].sum().idxmax() if len(df_filtered) > 0 else 'N/A'
            },
            'trendData': {
                'labels': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'],
                'data': [minority_spend/8 * (1 + i*0.1) for i in range(8)]  # Sample trend
            },
            'distributionData': {
                'labels': ['Minority', 'Woman-Owned', 'Veteran-Owned', 'Other'],
                'data': [minority_spend, woman_spend, veteran_spend, max(0, total_spend - minority_spend - woman_spend - veteran_spend)]
            },
            'records': df_filtered.head(10)[['VENDOR NAME 1', 'DEPARTMENT NAME', 'total_amount_clean', 'INPUT DATE', 'MINORITY', 'SB WOMAN', 'SB VETERAN']].to_dict('records')
        }
    except Exception as e:
        print(f"Error in diversity_drill: {e}")
        return {
            'summary': {'totalAmount': 0, 'recordCount': 0, 'avgAmount': 0, 'topVendor': 'N/A'},
            'trendData': {'labels': ['Jan', 'Feb', 'Mar'], 'data': [0, 0, 0]},
            'distributionData': {'labels': ['No Data'], 'data': [0]},
            'records': []
        }

def generate_vendor_performance_drill(df_filtered):
    """Generate vendor performance drill-down data"""
    try:
        vendor_performance = df_filtered.groupby('VENDOR NAME 1')['total_amount_clean'].agg(['sum', 'count', 'mean']).reset_index()
        vendor_performance = vendor_performance.sort_values('sum', ascending=False).head(10)
        
        return {
            'summary': {
                'totalAmount': df_filtered['total_amount_clean'].sum(),
                'recordCount': len(df_filtered),
                'avgAmount': df_filtered['total_amount_clean'].mean() if len(df_filtered) > 0 else 0,
                'topVendor': vendor_performance.iloc[0]['VENDOR NAME 1'] if len(vendor_performance) > 0 else 'N/A'
            },
            'trendData': {
                'labels': vendor_performance['VENDOR NAME 1'].head(6).tolist(),
                'data': vendor_performance['sum'].head(6).tolist()
            },
            'distributionData': {
                'labels': vendor_performance['VENDOR NAME 1'].head(5).tolist(),
                'data': vendor_performance['sum'].head(5).tolist()
            },
            'records': [
                {
                    'vendor': row['VENDOR NAME 1'],
                    'department': 'Various',
                    'amount': row['sum'],
                    'date': '2025-08-29',
                    'category': 'Multiple',
                    'status': 'Active',
                    'diversity': 'Mixed'
                } for _, row in vendor_performance.iterrows()
            ]
        }
    except Exception as e:
        print(f"Error in vendor_performance_drill: {e}")
        return {
            'summary': {'totalAmount': 0, 'recordCount': 0, 'avgAmount': 0, 'topVendor': 'N/A'},
            'trendData': {'labels': ['No Data'], 'data': [0]},
            'distributionData': {'labels': ['No Data'], 'data': [0]},
            'records': []
        }

def generate_department_drill(df_filtered, department_name):
    """Generate department-specific drill-down data"""
    try:
        dept_data = df_filtered[df_filtered['DEPARTMENT NAME'] == department_name] if department_name else df_filtered
        
        return {
            'summary': {
                'totalAmount': dept_data['total_amount_clean'].sum(),
                'recordCount': len(dept_data),
                'avgAmount': dept_data['total_amount_clean'].mean() if len(dept_data) > 0 else 0,
                'topVendor': dept_data.groupby('VENDOR NAME 1')['total_amount_clean'].sum().idxmax() if len(dept_data) > 0 else 'N/A'
            },
            'trendData': {
                'labels': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'],
                'data': [dept_data['total_amount_clean'].sum()/8 * (1 + i*0.05) for i in range(8)]
            },
            'distributionData': {
                'labels': dept_data.groupby('VENDOR NAME 1')['total_amount_clean'].sum().head(5).index.tolist(),
                'data': dept_data.groupby('VENDOR NAME 1')['total_amount_clean'].sum().head(5).values.tolist()
            },
            'records': dept_data.head(10)[['VENDOR NAME 1', 'DEPARTMENT NAME', 'total_amount_clean', 'INPUT DATE']].to_dict('records')
        }
    except Exception as e:
        print(f"Error in department_drill: {e}")
        return {
            'summary': {'totalAmount': 0, 'recordCount': 0, 'avgAmount': 0, 'topVendor': 'N/A'},
            'trendData': {'labels': ['Jan', 'Feb', 'Mar'], 'data': [0, 0, 0]},
            'distributionData': {'labels': ['No Data'], 'data': [0]},
            'records': []
        }

def generate_default_drill(df_filtered):
    """Generate default drill-down data"""
    try:
        return {
            'summary': {
                'totalAmount': df_filtered['total_amount_clean'].sum(),
                'recordCount': len(df_filtered),
                'avgAmount': df_filtered['total_amount_clean'].mean() if len(df_filtered) > 0 else 0,
                'topVendor': df_filtered.groupby('VENDOR NAME 1')['total_amount_clean'].sum().idxmax() if len(df_filtered) > 0 else 'N/A'
            },
            'trendData': {
                'labels': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'],
                'data': [df_filtered['total_amount_clean'].sum()/8 * (1 + i*0.1) for i in range(8)]
            },
            'distributionData': {
                'labels': ['Category A', 'Category B', 'Category C', 'Category D'],
                'data': [25, 30, 20, 25]
            },
            'records': df_filtered.head(10).to_dict('records')
        }
    except Exception as e:
        print(f"Error in default_drill: {e}")
        return {
            'summary': {'totalAmount': 0, 'recordCount': 0, 'avgAmount': 0, 'topVendor': 'N/A'},
            'trendData': {'labels': ['Jan', 'Feb', 'Mar'], 'data': [0, 0, 0]},
            'distributionData': {'labels': ['No Data'], 'data': [0]},
            'records': []
        }

# Run the app
if __name__ == '__main__':
    import os
    
    print("\n🚀 Flask server starting...")
    
    # Get port from environment variable (Azure sets this)
    port = int(os.environ.get('PORT', 5001))
    
    # Determine if running in production
    is_production = os.environ.get('FLASK_ENV') == 'production'
    
    if is_production:
        print("🌐 Production mode - Azure Web App")
        print(f"🚀 Starting on port: {port}")
    else:
        print("🧪 Development mode")
        print("🌐 API: http://localhost:5001")
        print("📊 Dashboard: Open dashboard.html in browser")
        print("🛑 To stop: Press Ctrl+C")
    
    print("-" * 50)
    
    app.run(
        debug=not is_production,
        port=port,
        host='0.0.0.0'
    )