# Drill-Down Report Features

## Overview
The procurement dashboard now includes comprehensive drill-down functionality that allows users to click on KPI cards and charts to access detailed reports.

## Available Drill-Down Reports

### 1. KPI Card Drill-Downs
- **Total Spend Card**: Click to view transaction details with sample data
- **Total Transactions**: Click to view detailed transaction list
- **Average Transaction Size**: Click to view transaction size analysis by ranges
- **Active Vendors**: Click to view vendor analysis with top vendors
- **Top 5 Vendor Concentration**: Click to view vendor concentration details
- **Minority-Owned Business %**: Click to view diversity analysis breakdown

### 2. Chart Click Interactions
- **Monthly Spending Trend Chart**: Click any data point to drill into that month's transactions
- **Top Vendors Chart**: Click any bar to see detailed vendor information
- **Diversity Chart**: Click any slice to see diversity category breakdown
- **Department Chart**: Click any slice to see department-specific analysis

## Drill-Down Modal Features

### Summary Cards
Each drill-down shows 4 summary metrics relevant to the selected data:
- Key performance indicators
- Totals and averages
- Percentages and ratios
- Monthly or category breakdowns

### Data Tables
Detailed tabular data with:
- Realistic sample data based on actual procurement patterns
- Appropriate headers for each drill-down type
- Formatted currency and numbers
- Relevant business metrics

### Export Functionality
- **CSV Export**: Download drill-down data as CSV file
- **Excel Export**: Download drill-down data as Excel file
- Automatic filename generation based on report type

## Drill-Down Types

### 1. Transaction Details
- Transaction ID, Date, Vendor, Department
- Amount, Status, Diversity flag
- Sample of 20 recent transactions

### 2. Vendor Analysis
- Top vendors ranked by spend
- Transaction counts and averages
- Vendor type (Diverse/Traditional)
- Status (Active/Inactive)

### 3. Diversity Analysis
- Breakdown by diversity categories
- Spend amounts and percentages
- Vendor counts per category
- Average spend per vendor type

### 4. Transaction Size Analysis
- Amount ranges (Under $1K to Over $1M)
- Transaction counts and percentages
- Average amounts per range
- Total values and monthly averages

### 5. Department Analysis
- Department-specific metrics
- Top vendors for the department
- Transaction volumes
- Last transaction dates

## Filter Integration
- All drill-down reports respect current filter settings
- Shows "(Filtered)" indicator when filters are active
- Data adjusts based on:
  - Date range filters
  - Amount range filters
  - Department filters
  - Diversity filters
  - Status filters

## Technical Implementation
- Modal-based interface for clean user experience
- Responsive design works on all screen sizes
- Click handlers on all charts and KPI cards
- Realistic data simulation based on filter selections
- Export functionality using browser download APIs
- Clean modal close on outside clicks or close button

## Usage Instructions
1. **Click any KPI card** with the drill icon to open detailed analysis
2. **Click any chart element** (bars, lines, pie slices) for specific breakdowns
3. **Use Export buttons** to download data as CSV or Excel
4. **Apply filters first** to get filtered drill-down reports
5. **Click outside modal** or close button to return to dashboard

## Benefits
- **Enhanced Analysis**: Deep dive into specific data points
- **Export Capability**: Take data for further analysis
- **Filter Awareness**: Consistent with dashboard filter state
- **Interactive Charts**: Charts become actionable interfaces
- **Professional Reports**: Clean, formatted drill-down views
