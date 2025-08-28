# 🏢 Procurement Dashboard

A comprehensive, interactive procurement analytics dashboard built with Flask and modern web technologies. Features real-time data visualization, advanced filtering, drill-down reporting, and meaningful KPIs for procurement management.

![Dashboard Preview](https://img.shields.io/badge/Status-Active-green) ![Python](https://img.shields.io/badge/Python-3.11-blue) ![Flask](https://img.shields.io/badge/Flask-Latest-red) ![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow)

## 🌟 Features

### 📊 **Interactive Dashboard**
- **8 Professional KPIs**: Cost savings, cycle time, vendor performance, compliance rate, etc.
- **4 Dynamic Charts**: Spending trends, vendor analysis, diversity metrics, department breakdown
- **Real-time Filtering**: Date range, amount, department, diversity, and status filters
- **Responsive Design**: Optimized for desktop, tablet, and mobile devices

### 🔍 **Advanced Analytics**
- **Drill-down Reports**: Click any KPI or chart element for detailed analysis
- **YTD/MTD Views**: Switch between yearly and monthly spending trends
- **Export Capabilities**: Download reports as CSV or Excel files
- **Filter Integration**: All drill-downs respect active filter settings

### 💼 **Business Intelligence**
- **Spend Performance Analysis**: Budget variance and category breakdown
- **Vendor Performance Scorecards**: Delivery, quality, and cost metrics
- **Risk Assessment**: Supply chain risk monitoring and mitigation
- **Diversity Tracking**: Supplier diversity goals and progress

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Git (for cloning repository)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/procurement-dashboard.git
   cd procurement-dashboard
   ```

2. **Create virtual environment**
   ```bash
   python -m venv dashboard_env
   
   # Windows
   dashboard_env\Scripts\activate
   
   # macOS/Linux
   source dashboard_env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask flask-cors pandas numpy
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the dashboard**
   - API: http://localhost:5001
   - Dashboard: Open `dashboard.html` in your browser

## 📁 Project Structure

```
procurement-dashboard/
├── app.py                      # Flask backend API
├── dashboard.html              # Main dashboard interface
├── Purchase data.csv           # Sample procurement data (145MB, 306K+ records)
├── test_simple.html           # Simple test interface
├── dashboard_env/             # Python virtual environment
├── README.md                  # Project documentation
├── DRILL_DOWN_FEATURES.md     # Drill-down functionality guide
├── ENHANCED_KPIS.md           # KPI documentation
└── YTD_MTD_ENHANCEMENT.md     # Time period filter guide
```

## 🎯 Key Performance Indicators (KPIs)

| KPI | Description | Business Value |
|-----|-------------|----------------|
| 💰 **Total YTD Spend** | Year-to-date procurement spending | Budget monitoring |
| 📉 **Cost Savings** | Procurement savings achieved | ROI demonstration |
| ⏱️ **Cycle Time** | Average procurement process time | Efficiency tracking |
| 🎯 **Vendor Performance** | Supplier quality and reliability | Vendor management |
| 📋 **Contract Compliance** | Adherence to contract terms | Risk mitigation |
| 🤝 **Diversity Index** | Supplier diversity percentage | Corporate goals |
| ⚠️ **Risk Score** | Supply chain risk assessment | Proactive management |
| 🚨 **Emergency Purchases** | Unplanned procurement percentage | Process improvement |

## 📊 Dashboard Features

### Interactive Charts
- **Monthly Spending Trend**: YTD/MTD toggle with clickable data points
- **Top Vendors**: Vendor spend ranking with performance drill-down
- **Diversity Metrics**: Pie chart showing supplier diversity breakdown
- **Department Analysis**: Spending distribution by department

### Advanced Filtering
- **Date Ranges**: YTD, 2024, Last 30/90 days, custom ranges
- **Amount Ranges**: Under $1K to Over $1M transaction filtering
- **Departments**: Filter by specific departments
- **Diversity**: Minority, woman, veteran-owned business filters
- **Status**: Filter by document status (Posted, Created, Approved)

### Drill-down Reporting
- **Transaction Details**: Sample transactions with vendor and department info
- **Vendor Analysis**: Top vendor performance with metrics
- **Savings Breakdown**: Cost savings by initiative type
- **Risk Assessment**: Supply chain risk categories and mitigation

## 🔧 Technical Stack

### Backend
- **Flask**: Lightweight Python web framework
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Flask-CORS**: Cross-origin resource sharing

### Frontend
- **HTML5/CSS3**: Modern responsive design
- **JavaScript ES6**: Interactive functionality
- **Chart.js**: Dynamic data visualization
- **CSS Grid/Flexbox**: Responsive layouts

### Data
- **CSV Processing**: Large dataset handling (306K+ records)
- **Real-time Filtering**: Dynamic data manipulation
- **Export Functions**: CSV and Excel download capabilities

## 🌐 GitHub Pages Deployment

To deploy the dashboard on GitHub Pages:

1. **Enable GitHub Pages** in repository settings
2. **Access the dashboard** at: `https://yourusername.github.io/procurement-dashboard/dashboard.html`
3. **API Considerations**: Backend API requires separate hosting (Heroku, Vercel, etc.)

## 📈 Usage Examples

### Executive Dashboard
- Monitor total YTD spend and cost savings
- Track vendor performance and compliance rates
- Assess supply chain risks and emergency purchases

### Procurement Management
- Analyze spending trends and cycle times
- Review vendor scorecards and performance metrics
- Monitor diversity goals and supplier distribution

### Financial Analysis
- Export detailed spending reports
- Analyze budget variances by category
- Track procurement savings initiatives

## 🔍 Data Sources

The dashboard includes:
- **306,912 procurement transactions**
- **3,774 unique vendors**
- **$3.07B total procurement spend**
- **Multiple departments and categories**
- **Diversity and compliance flags**

## 🚀 Future Enhancements

### Planned Features
- [ ] Real-time data integration
- [ ] Advanced predictive analytics
- [ ] Custom dashboard builder
- [ ] Mobile app version
- [ ] Multi-tenant support

### API Extensions
- [ ] RESTful API documentation
- [ ] GraphQL integration
- [ ] Real-time WebSocket updates
- [ ] Third-party system integrations

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with modern web technologies and best practices
- Designed for enterprise procurement management
- Focused on actionable business intelligence

## 📞 Support

For questions, issues, or feature requests:
- 📧 Create an issue in this repository
- 💬 Contact the development team
- 📖 Check the documentation files

---

**Built with ❤️ for modern procurement management**
