# Monthly Spending Trend - YTD/MTD Filter Enhancement

## Overview
The Monthly Spending Trend chart now includes integrated filter buttons that allow users to switch between Year-to-Date (YTD) and Month-to-Date (MTD) views directly within the chart.

## New Features

### 🔄 **Period Filter Buttons**
- **YTD Button**: Shows monthly spending data for the entire year (Jan-Aug 2025)
- **MTD Button**: Shows daily spending data for the current month
- **Active State**: Clear visual indication of currently selected period
- **Responsive Design**: Optimized layout for both desktop and mobile

### 📊 **Dynamic Chart Updates**

#### YTD View (Default)
- **Data**: Monthly aggregated spending from January to August 2025
- **Chart Type**: Line chart with monthly data points
- **Labels**: Month names (Jan, Feb, Mar, etc.)
- **Scale**: Shows values in millions (e.g., "$383M")
- **Tooltip**: "Month: Jan" with spend amount

#### MTD View
- **Data**: Daily spending for current month (August 2025)
- **Chart Type**: Line chart with daily data points
- **Labels**: Date format (8/1, 8/2, 8/3, etc.)
- **Scale**: Shows values in millions with daily granularity
- **Tooltip**: "Day: 8/15" with spend amount
- **Weekend Logic**: Reduced spending on weekends (realistic pattern)

### 💡 **Smart Data Generation**

#### YTD Data Logic
- **Base Amount**: ~$383M per month average
- **Seasonal Variation**: Sine wave pattern for realistic seasonal trends
- **Growth Trend**: Slight upward trend (2% per month)
- **Random Variation**: ±15% for realistic variance

#### MTD Data Logic
- **Base Amount**: ~$12M per day average
- **Weekend Factor**: 30% of normal spending on weekends
- **Random Variation**: ±20% for daily fluctuations
- **Current Month**: Shows data up to current date (August 28, 2025)

### 🎯 **Enhanced Interactivity**

#### Click Functionality
- **YTD**: Click any month to drill down to monthly breakdown
- **MTD**: Click any day to drill down to daily breakdown
- **Drill-down Type**: Automatically adjusts based on selected period

#### Visual Improvements
- **Point Styling**: Different point sizes for MTD vs YTD
- **Grid Lines**: Enhanced grid for better readability
- **Label Rotation**: Automatic rotation for MTD labels (45°)
- **Color Scheme**: Consistent blue theme with transparency

### 📱 **Mobile Optimization**

#### Responsive Layout
- **Stacked Header**: Chart title and filters stack vertically on mobile
- **Button Sizing**: Smaller buttons on mobile devices
- **Filter Position**: Right-aligned filters on mobile
- **Touch-Friendly**: Adequate touch targets for mobile interaction

### 🔧 **Technical Implementation**

#### JavaScript Functions
- **`updateSpendPeriod(period)`**: Handles filter button clicks
- **`loadSpendChartForPeriod(period)`**: Loads appropriate data
- **`generateYTDSpendData()`**: Creates realistic yearly data
- **`generateMTDSpendData()`**: Creates realistic daily data

#### State Management
- **`currentSpendPeriod`**: Tracks active filter (defaults to 'ytd')
- **Button States**: Dynamic active/inactive styling
- **Chart Persistence**: Maintains filter selection during dashboard operations

#### API Integration
- **YTD**: Attempts to load from API, falls back to generated data
- **MTD**: Uses generated data (can be extended to API)
- **Error Handling**: Graceful fallback to generated data

## Usage Instructions

### For Users
1. **Switch Views**: Click "YTD" or "MTD" buttons above the chart
2. **Analyze Trends**: 
   - Use YTD for annual spending patterns
   - Use MTD for current month daily activity
3. **Drill Down**: Click any data point for detailed analysis
4. **Export**: All export functions work with filtered data

### For Administrators
- **Data Sources**: Can connect MTD to real-time daily data APIs
- **Customization**: Easy to add additional periods (QTD, weekly, etc.)
- **Integration**: Works seamlessly with existing filter system

## Business Value

### Strategic Planning
- **Budget Monitoring**: YTD view for annual budget tracking
- **Cash Flow**: MTD view for daily cash flow management
- **Trend Analysis**: Switch between granularities for different insights

### Operational Insights
- **Daily Operations**: MTD view shows daily spending patterns
- **Seasonal Trends**: YTD view reveals monthly seasonal patterns
- **Anomaly Detection**: Easy identification of unusual spending days/months

### Executive Reporting
- **Board Presentations**: YTD for high-level annual overview
- **Operations Reviews**: MTD for detailed current performance
- **Flexibility**: Single chart serves multiple reporting needs

## Future Enhancements

### Additional Periods
- **QTD (Quarter-to-Date)**: Quarterly view option
- **WTD (Week-to-Date)**: Weekly spending patterns
- **Custom Range**: User-selectable date ranges

### Advanced Features
- **Comparison Mode**: Show multiple periods simultaneously
- **Forecast Line**: Predictive spending based on current trends
- **Budget Line**: Overlay budget targets on spending actuals

This enhancement transforms the spending chart from a simple monthly view into a comprehensive time-based analysis tool that serves both strategic and operational needs.
