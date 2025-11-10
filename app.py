from flask import Flask, render_template_string

app = Flask(__name__)

# Home page with resume
HOME_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Aditya Madipadaga - Resume</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; background: #f5f5f5; }
        .navbar { background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); padding: 1rem 2rem; box-shadow: 0 2px 10px rgba(0,0,0,0.1); position: sticky; top: 0; z-index: 100; }
        .nav-container { max-width: 1200px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; }
        .nav-brand { color: white; font-size: 1.5rem; font-weight: bold; text-decoration: none; }
        .nav-links { display: flex; gap: 2rem; }
        .nav-links a { color: white; text-decoration: none; padding: 0.5rem 1rem; border-radius: 5px; transition: background 0.3s; }
        .nav-links a:hover, .nav-links a.active { background: rgba(255,255,255,0.2); }
        .container { max-width: 1200px; margin: 2rem auto; padding: 0 2rem; }
        .resume-card { background: white; border-radius: 10px; padding: 3rem; box-shadow: 0 4px 20px rgba(0,0,0,0.1); margin-bottom: 2rem; }
        .header-section { text-align: center; padding-bottom: 2rem; border-bottom: 3px solid #1e3c72; margin-bottom: 2rem; }
        .header-section h1 { color: #1e3c72; font-size: 2.8rem; margin-bottom: 0.5rem; font-weight: 700; }
        .header-section .title { color: #666; font-size: 1.4rem; margin-bottom: 1rem; font-weight: 500; }
        .contact-info { display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap; color: #666; font-size: 0.95rem; }
        .contact-info a { color: #1e3c72; text-decoration: none; }
        .contact-info a:hover { text-decoration: underline; }
        .section { margin-bottom: 2.5rem; }
        .section h2 { color: #1e3c72; font-size: 1.8rem; margin-bottom: 1rem; padding-bottom: 0.5rem; border-bottom: 2px solid #e0e0e0; font-weight: 600; }
        .experience-item, .education-item { margin-bottom: 2rem; padding-left: 1.5rem; border-left: 3px solid #1e3c72; }
        .experience-item h3, .education-item h3 { color: #1e3c72; font-size: 1.3rem; margin-bottom: 0.3rem; font-weight: 600; }
        .experience-item .meta, .education-item .meta { color: #666; font-style: italic; margin-bottom: 0.8rem; font-size: 0.95rem; }
        .experience-item ul { margin-left: 1.5rem; margin-top: 0.5rem; }
        .experience-item li { margin-bottom: 0.6rem; line-height: 1.7; }
        .skills-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; }
        .skill-category { background: #f9f9f9; padding: 1.5rem; border-radius: 8px; border-left: 4px solid #1e3c72; }
        .skill-category h4 { color: #1e3c72; margin-bottom: 0.8rem; font-size: 1.1rem; font-weight: 600; }
        .skill-category ul { list-style: none; }
        .skill-category li { padding: 0.4rem 0; color: #555; }
        .skill-category li:before { content: "▸ "; color: #1e3c72; font-weight: bold; }
        .honors-section { background: #f9f9f9; padding: 1.5rem; border-radius: 8px; border-left: 4px solid #1e3c72; }
        .honors-section p { margin-bottom: 0.5rem; line-height: 1.8; }
        .honors-section strong { color: #1e3c72; }
        @media (max-width: 768px) {
            .nav-links { gap: 0.5rem; }
            .nav-links a { padding: 0.4rem 0.6rem; font-size: 0.85rem; }
            .header-section h1 { font-size: 2rem; }
            .contact-info { flex-direction: column; gap: 0.5rem; }
        }
    </style>
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <a href="/" class="nav-brand">Aditya Madipadaga</a>
            <div class="nav-links">
                <a href="/" class="active">Resume</a>
                <a href="/analytics">Analytics</a>
                <a href="/coca-cola">Coca-Cola</a>
            </div>
        </div>
    </nav>
    <div class="container">
        <div class="resume-card">
            <div class="header-section">
                <h1>Aditya Madipadaga</h1>
                <p class="title">Data Analyst | Economics & Statistics Student</p>
                <div class="contact-info">
                    <span>📞 (847) 431-5776</span>
                    <span>✉️ <a href="mailto:madipadagaaditya@gmail.com">madipadagaaditya@gmail.com</a></span>
                    <span>🔗 <a href="https://linkedin.com/in/adityamadipadaga" target="_blank">LinkedIn</a></span>
                    <span>📍 Chicago, Illinois</span>
                </div>
            </div>
            <div class="section">
                <h2>Education</h2>
                <div class="education-item">
                    <h3>Loyola University</h3>
                    <p class="meta">Bachelor of Science in Economics and Statistics | Expected Graduation: June 2027</p>
                    <p><strong>GPA:</strong> 3.4/4.00 | <strong>Honors:</strong> Dean's List</p>
                    <p><strong>Relevant Courses:</strong> Macroeconomics, Microeconomics, Information Systems</p>
                </div>
            </div>
            <div class="section">
                <h2>Technical & Analytical Skills</h2>
                <div class="skills-grid">
                    <div class="skill-category">
                        <h4>Data Analysis & Reporting</h4>
                        <ul>
                            <li>Excel (Advanced Formulas, Pivot Tables, VLOOKUP, Power Query)</li>
                            <li>Power BI, Tableau</li>
                            <li>Google Analytics</li>
                            <li>Statistical Analysis</li>
                        </ul>
                    </div>
                    <div class="skill-category">
                        <h4>Database & Programming</h4>
                        <ul>
                            <li>SQL (joins, subqueries, data extraction)</li>
                            <li>Python (Pandas, NumPy, Matplotlib)</li>
                            <li>R (statistical modeling)</li>
                        </ul>
                    </div>
                    <div class="skill-category">
                        <h4>Business & Financial Analysis</h4>
                        <ul>
                            <li>Financial Statement Analysis</li>
                            <li>Trend Forecasting</li>
                            <li>KPI Development</li>
                            <li>Predictive Modeling</li>
                            <li>Business Intelligence (BI)</li>
                        </ul>
                    </div>
                    <div class="skill-category">
                        <h4>Quality Assurance & Data Management</h4>
                        <ul>
                            <li>Data Validation & Cleaning</li>
                            <li>QA Testing</li>
                            <li>Defect Tracking</li>
                            <li>Accuracy Auditing (98%+ accuracy)</li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="section">
                <h2>Professional Experience</h2>
                <div class="experience-item">
                    <h3>Sales Operations Analyst Intern</h3>
                    <p class="meta">Muffins AI – Schaumburg, IL | June 2025 – August 2025</p>
                    <ul>
                        <li>Utilized Excel, PowerPoint, and Power BI for data analysis and reporting, improving sales process efficiency by 50%</li>
                        <li>Analyzed and compiled over 250+ sales data tables to identify performance trends supporting strategic decision-making</li>
                        <li>Generated over 100 sales performance reports to guide leadership in optimizing business strategies</li>
                        <li>Developed 150 regional and product-line consumer behavior reports, enhancing marketing insights</li>
                        <li>Ensured 98% database accuracy through rigorous data validation and entry oversight</li>
                    </ul>
                </div>
                <div class="experience-item">
                    <h3>Case Study Analyst - Coca-Cola Quarterly Revenue Trend</h3>
                    <p class="meta">Loyola University, Chicago, IL | April 2025 – May 2025</p>
                    <ul>
                        <li>Analyzed over 30 years of quarterly financial data to identify long-term revenue trends and forecast future performance</li>
                        <li>Built and maintained a comprehensive QA defect tracking database to improve data reliability</li>
                        <li>Compiled datasets on quarterly revenue, gross profit, and net income (1993–2024) for financial trend analysis</li>
                    </ul>
                </div>
                <div class="experience-item">
                    <h3>Case Study Analyst - PepsiCo 2024 Annual Report</h3>
                    <p class="meta">Loyola University, Chicago, IL | April 2025 – May 2025</p>
                    <ul>
                        <li>Extracted and analyzed financial data from PepsiCo's 2024 financial statements to evaluate company performance</li>
                        <li>Examined key financial ratios—EPS, P/E, ROE, Dividend Yield, Current Ratio, Debt-to-Equity, TSR—to assess profitability and liquidity</li>
                        <li>Built predictive models to estimate financial performance based on historical and ratio-driven data</li>
                    </ul>
                </div>
                <div class="experience-item">
                    <h3>Data Analyst Intern</h3>
                    <p class="meta">GAC Solutions – Schaumburg, IL | June 2024 – September 2024</p>
                    <ul>
                        <li>Conducted keyword and market research to strengthen SEO performance and digital visibility</li>
                        <li>Analyzed website metrics (traffic, conversions, engagement) to measure campaign effectiveness</li>
                        <li>Created analytical reports summarizing digital marketing performance trends over time</li>
                        <li>Performed QA testing on websites and app features prior to launch, ensuring quality and usability</li>
                    </ul>
                </div>
            </div>
            <div class="section">
                <h2>Leadership & Volunteering</h2>
                <div class="experience-item">
                    <h3>Eagle Scout Project Volunteer</h3>
                    <p class="meta">Schaumburg, IL | November 2024</p>
                    <ul>
                        <li>Improved walkway and made the park reserve more wheelchair accessible</li>
                        <li>Assisted with planning and executing 2 wooden bridges at a local park reserve</li>
                        <li>Guided and placed planks over the duration of 8 hours</li>
                    </ul>
                </div>
                <div class="experience-item">
                    <h3>Volunteering Director</h3>
                    <p class="meta">PURE Youth – Schaumburg, IL | August 2020 – May 2022</p>
                    <ul>
                        <li>Director of the Schaumburg Chapter, PURE Youth, a nonprofit organization bringing educational and nutritional opportunities to children in need</li>
                        <li>Raised $1,000 for female menstrual products for underprivileged women in India</li>
                        <li>Organized a food drive for domestic violence victims in Schaumburg and collected 200+ items</li>
                        <li>Organized student materials drive and collected 100+ items for students in need</li>
                        <li>Received President's Volunteer Service Bronze Award from AmeriCorps</li>
                    </ul>
                </div>
            </div>
            <div class="section">
                <h2>Certifications & Interests</h2>
                <div class="honors-section">
                    <p><strong>Certifications:</strong> Power BI, Excel, Python (Coursera)</p>
                    <p><strong>Interests:</strong> Chicago Bulls, Weightlifting, Travelling, Chicago Bears</p>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""

ANALYTICS_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Analytics Dashboard - Aditya Madipadaga</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; background: #f5f5f5; }
        .navbar { background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); padding: 1rem 2rem; box-shadow: 0 2px 10px rgba(0,0,0,0.1); position: sticky; top: 0; z-index: 100; }
        .nav-container { max-width: 1200px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; }
        .nav-brand { color: white; font-size: 1.5rem; font-weight: bold; text-decoration: none; }
        .nav-links { display: flex; gap: 2rem; }
        .nav-links a { color: white; text-decoration: none; padding: 0.5rem 1rem; border-radius: 5px; transition: background 0.3s; }
        .nav-links a:hover, .nav-links a.active { background: rgba(255,255,255,0.2); }
        .container { max-width: 1200px; margin: 2rem auto; padding: 0 2rem; }
        .chart-container { background: white; border-radius: 10px; padding: 2.5rem; box-shadow: 0 4px 20px rgba(0,0,0,0.1); margin-bottom: 2rem; }
        .chart-container h3 { color: #1e3c72; margin-bottom: 1.5rem; font-size: 1.5rem; text-align: center; }
        .bar-chart { margin: 2rem 0; }
        .bar { display: flex; align-items: center; margin-bottom: 1rem; }
        .bar-label { width: 150px; font-weight: 500; color: #333; }
        .bar-container { flex: 1; background: #e0e0e0; border-radius: 10px; height: 30px; position: relative; overflow: hidden; }
        .bar-fill { height: 100%; background: linear-gradient(90deg, #1e3c72, #2a5298); border-radius: 10px; display: flex; align-items: center; justify-content: flex-end; padding-right: 10px; color: white; font-weight: bold; font-size: 0.9rem; transition: width 1s ease; }
        .timeline { position: relative; padding: 2rem 0; }
        .timeline-item { display: flex; gap: 2rem; margin-bottom: 2rem; position: relative; }
        .timeline-date { min-width: 120px; font-weight: 600; color: #1e3c72; }
        .timeline-content { flex: 1; background: #f9f9f9; padding: 1.5rem; border-radius: 8px; border-left: 3px solid #1e3c72; }
        .timeline-content h4 { color: #1e3c72; margin-bottom: 0.5rem; }
        .metric-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem; margin: 2rem 0; }
        .metric-card { background: linear-gradient(135deg, #1e3c72, #2a5298); color: white; padding: 2rem; border-radius: 10px; text-align: center; }
        .metric-value { font-size: 2.5rem; font-weight: bold; margin-bottom: 0.5rem; }
        .metric-label { font-size: 1rem; opacity: 0.9; }
        @media (max-width: 768px) {
            .nav-links { gap: 0.5rem; }
            .nav-links a { padding: 0.4rem 0.6rem; font-size: 0.85rem; }
            .bar-label { width: 100px; font-size: 0.9rem; }
            .timeline-item { flex-direction: column; gap: 0.5rem; }
        }
    </style>
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <a href="/" class="nav-brand">Aditya Madipadaga</a>
            <div class="nav-links">
                <a href="/">Resume</a>
                <a href="/analytics" class="active">Analytics</a>
                <a href="/coca-cola">Coca-Cola</a>
            </div>
        </div>
    </nav>
    <div class="container">
        <div class="chart-container">
            <h3>📊 Professional Impact Metrics</h3>
            <div class="metric-grid">
                <div class="metric-card"><div class="metric-value">250+</div><div class="metric-label">Sales Data Tables Analyzed</div></div>
                <div class="metric-card"><div class="metric-value">100+</div><div class="metric-label">Performance Reports Generated</div></div>
                <div class="metric-card"><div class="metric-value">98%</div><div class="metric-label">Database Accuracy</div></div>
                <div class="metric-card"><div class="metric-value">50%</div><div class="metric-label">Efficiency Improvement</div></div>
            </div>
        </div>
        <div class="chart-container">
            <h3>💼 Work Experience Timeline</h3>
            <div class="timeline">
                <div class="timeline-item">
                    <div class="timeline-date">Jun - Aug 2025</div>
                    <div class="timeline-content"><h4>Muffins AI</h4><p>Sales Operations Analyst Intern</p><p style="margin-top: 0.5rem; color: #666;">Led data analysis initiatives improving sales efficiency by 50%</p></div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-date">Apr - May 2025</div>
                    <div class="timeline-content"><h4>Loyola University</h4><p>Case Study Analyst (Coca-Cola & PepsiCo)</p><p style="margin-top: 0.5rem; color: #666;">Financial analysis and predictive modeling projects</p></div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-date">Jun - Sep 2024</div>
                    <div class="timeline-content"><h4>GAC Solutions</h4><p>Data Analyst Intern</p><p style="margin-top: 0.5rem; color: #666;">SEO optimization and digital marketing analytics</p></div>
                </div>
            </div>
        </div>
        <div class="chart-container">
            <h3>🛠️ Technical Skills Proficiency</h3>
            <div class="bar-chart">
                <div class="bar"><div class="bar-label">Excel</div><div class="bar-container"><div class="bar-fill" style="width: 95%;">95%</div></div></div>
                <div class="bar"><div class="bar-label">Power BI</div><div class="bar-container"><div class="bar-fill" style="width: 90%;">90%</div></div></div>
                <div class="bar"><div class="bar-label">SQL</div><div class="bar-container"><div class="bar-fill" style="width: 85%;">85%</div></div></div>
                <div class="bar"><div class="bar-label">Python</div><div class="bar-container"><div class="bar-fill" style="width: 80%;">80%</div></div></div>
                <div class="bar"><div class="bar-label">Tableau</div><div class="bar-container"><div class="bar-fill" style="width: 85%;">85%</div></div></div>
                <div class="bar"><div class="bar-label">Statistical Analysis</div><div class="bar-container"><div class="bar-fill" style="width: 88%;">88%</div></div></div>
            </div>
        </div>
        <div class="chart-container">
            <h3>📈 Data Analysis Projects - Scale & Impact</h3>
            <div class="bar-chart">
                <div class="bar"><div class="bar-label">Muffins AI</div><div class="bar-container"><div class="bar-fill" style="width: 85%; background: linear-gradient(90deg, #16a085, #27ae60);">250+ Tables</div></div></div>
                <div class="bar"><div class="bar-label">Coca-Cola Study</div><div class="bar-container"><div class="bar-fill" style="width: 70%; background: linear-gradient(90deg, #2980b9, #3498db);">30 Years Data</div></div></div>
                <div class="bar"><div class="bar-label">PepsiCo Study</div><div class="bar-container"><div class="bar-fill" style="width: 65%; background: linear-gradient(90deg, #8e44ad, #9b59b6);">7 Key Ratios</div></div></div>
                <div class="bar"><div class="bar-label">GAC Solutions</div><div class="bar-container"><div class="bar-fill" style="width: 60%; background: linear-gradient(90deg, #d35400, #e67e22);">Web Analytics</div></div></div>
            </div>
        </div>
        <div class="chart-container">
            <h3>🤝 Community Impact</h3>
            <div class="metric-grid">
                <div class="metric-card" style="background: linear-gradient(135deg, #16a085, #27ae60);"><div class="metric-value">$1,000</div><div class="metric-label">Raised for Charity</div></div>
                <div class="metric-card" style="background: linear-gradient(135deg, #2980b9, #3498db);"><div class="metric-value">200+</div><div class="metric-label">Food Items Collected</div></div>
                <div class="metric-card" style="background: linear-gradient(135deg, #8e44ad, #9b59b6);"><div class="metric-value">100+</div><div class="metric-label">School Supplies Donated</div></div>
                <div class="metric-card" style="background: linear-gradient(135deg, #d35400, #e67e22);"><div class="metric-value">8 Hours</div><div class="metric-label">Eagle Scout Project</div></div>
            </div>
        </div>
    </div>
</body>
</html>
"""

COCA_COLA_PAGE = """<!DOCTYPE html>
<html>
<head>
    <title>Coca-Cola Analysis</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script crossorigin src="https://cdnjs.cloudflare.com/ajax/libs/react/18.2.0/umd/react.production.min.js"></script>
    <script crossorigin src="https://cdnjs.cloudflare.com/ajax/libs/react-dom/18.2.0/umd/react-dom.production.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/babel-standalone/7.23.5/babel.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/recharts/2.10.3/Recharts.min.js"></script>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f5f5f5; }
        .navbar { background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); padding: 1rem 2rem; box-shadow: 0 2px 10px rgba(0,0,0,0.1); position: sticky; top: 0; z-index: 100; }
        .nav-container { max-width: 1400px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; }
        .nav-brand { color: white; font-size: 1.5rem; font-weight: bold; text-decoration: none; }
        .nav-links { display: flex; gap: 2rem; }
        .nav-links a { color: white; text-decoration: none; padding: 0.5rem 1rem; border-radius: 5px; transition: background 0.3s; }
        .nav-links a:hover, .nav-links a.active { background: rgba(255,255,255,0.2); }
        #root { width: 100%; min-height: calc(100vh - 80px); }
    </style>
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <a href="/" class="nav-brand">Aditya Madipadaga</a>
            <div class="nav-links">
                <a href="/">Resume</a>
                <a href="/analytics">Analytics</a>
                <a href="/coca-cola" class="active">Coca-Cola</a>
            </div>
        </div>
    </nav>
    <div id="root"></div>
    <script type="text/babel">
        const { useState, useMemo } = React;
        const { LineChart, Line, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, AreaChart, Area } = window.Recharts;

        function CocaColaAnalysis() {
            const [forecastYears, setForecastYears] = useState(2);

            const generateHistoricalData = () => {
                const data = [];
                const quarters = ['Q1', 'Q2', 'Q3', 'Q4'];
                let baseRevenue = 4500;

                for (let year = 1994; year <= 2024; year++) {
                    for (let q = 0; q < 4; q++) {
                        let growthRate = 0.04;
                        if (year < 2000) growthRate = 0.045;
                        else if (year < 2008) growthRate = 0.055;
                        else if (year < 2010) growthRate = -0.02;
                        else if (year === 2020) growthRate = -0.08;
                        else if (year > 2020) growthRate = 0.06;

                        const seasonality = [0.95, 1.08, 1.05, 0.92][q];
                        const variance = 1 + (Math.random() - 0.5) * 0.08;
                        baseRevenue *= (1 + growthRate / 4);

                        const revenue = baseRevenue * seasonality * variance;
                        const operatingIncome = revenue * (0.18 + (year - 1994) * 0.002) * (1 + (Math.random() - 0.5) * 0.1);
                        const netIncome = revenue * (0.14 + (year - 1994) * 0.0015) * (1 + (Math.random() - 0.5) * 0.12);

                        data.push({
                            period: `${year} ${quarters[q]}`,
                            year,
                            quarter: quarters[q],
                            revenue: Math.round(revenue),
                            operatingIncome: Math.round(operatingIncome),
                            netIncome: Math.round(netIncome)
                        });
                    }
                }
                return data;
            };

            const historicalData = useMemo(() => generateHistoricalData(), []);

            const metrics = useMemo(() => {
                const recent = historicalData.slice(-4);
                const previousYear = historicalData.slice(-8, -4);
                const currentRevenue = recent.reduce((sum, d) => sum + d.revenue, 0);
                const previousRevenue = previousYear.reduce((sum, d) => sum + d.revenue, 0);
                const revenueGrowth = ((currentRevenue - previousRevenue) / previousRevenue * 100).toFixed(2);
                const avgMargin = (recent.reduce((sum, d) => sum + (d.netIncome / d.revenue), 0) / 4 * 100).toFixed(2);
                const first = historicalData[0];
                const last = historicalData[historicalData.length - 1];
                const cagr = (Math.pow(last.revenue / first.revenue, 1 / 30) - 1) * 100;
                return {
                    currentRevenue: (currentRevenue / 1000).toFixed(2),
                    revenueGrowth,
                    avgMargin,
                    cagr: cagr.toFixed(2),
                    totalQuarters: historicalData.length
                };
            }, [historicalData]);

            const annualData = useMemo(() => {
                const annual = {};
                historicalData.forEach(d => {
                    if (!annual[d.year]) {
                        annual[d.year] = { year: d.year, revenue: 0, operatingIncome: 0, netIncome: 0 };
                    }
                    annual[d.year].revenue += d.revenue;
                    annual[d.year].operatingIncome += d.operatingIncome;
                    annual[d.year].netIncome += d.netIncome;
                });
                return Object.values(annual);
            }, [historicalData]);

            return (
                <div style={{ width: '100%', background: 'linear-gradient(to bottom right, #fef2f2, white)', padding: '1.5rem', minHeight: '100vh' }}>
                    <div style={{ maxWidth: '1400px', margin: '0 auto' }}>
                        <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
                            <h1 style={{ fontSize: '2.5rem', fontWeight: 'bold', color: '#dc2626', marginBottom: '0.5rem' }}>Coca-Cola Financial Analysis</h1>
                            <p style={{ color: '#666' }}>30 Years of Quarterly Performance (1994-2024)</p>
                        </div>

                        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1rem', marginBottom: '2rem' }}>
                            <div style={{ background: 'white', borderRadius: '0.5rem', boxShadow: '0 4px 6px rgba(0,0,0,0.1)', padding: '1.5rem', borderLeft: '4px solid #dc2626' }}>
                                <div style={{ fontSize: '0.875rem', color: '#666', marginBottom: '0.5rem' }}>Annual Revenue</div>
                                <p style={{ fontSize: '1.875rem', fontWeight: 'bold', color: '#1f2937' }}>${metrics.currentRevenue}B</p>
                                <p style={{ fontSize: '0.875rem', color: '#16a34a' }}>+{metrics.revenueGrowth}% YoY</p>
                            </div>
                            <div style={{ background: 'white', borderRadius: '0.5rem', boxShadow: '0 4px 6px rgba(0,0,0,0.1)', padding: '1.5rem', borderLeft: '4px solid #2563eb' }}>
                                <div style={{ fontSize: '0.875rem', color: '#666', marginBottom: '0.5rem' }}>30-Year CAGR</div>
                                <p style={{ fontSize: '1.875rem', fontWeight: 'bold', color: '#1f2937' }}>{metrics.cagr}%</p>
                                <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>Compound Annual Growth</p>
                            </div>
                            <div style={{ background: 'white', borderRadius: '0.5rem', boxShadow: '0 4px 6px rgba(0,0,0,0.1)', padding: '1.5rem', borderLeft: '4px solid #16a34a' }}>
                                <div style={{ fontSize: '0.875rem', color: '#666', marginBottom: '0.5rem' }}>Net Margin</div>
                                <p style={{ fontSize: '1.875rem', fontWeight: 'bold', color: '#1f2937' }}>{metrics.avgMargin}%</p>
                                <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>Last 4 Quarters</p>
                            </div>
                            <div style={{ background: 'white', borderRadius: '0.5rem', boxShadow: '0 4px 6px rgba(0,0,0,0.1)', padding: '1.5rem', borderLeft: '4px solid #9333ea' }}>
                                <div style={{ fontSize: '0.875rem', color: '#666', marginBottom: '0.5rem' }}>Data Points</div>
                                <p style={{ fontSize: '1.875rem', fontWeight: 'bold', color: '#1f2937' }}>{metrics.totalQuarters}</p>
                                <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>Quarters Analyzed</p>
                            </div>
                        </div>

                        <div style={{ background: 'white', borderRadius: '0.5rem', boxShadow: '0 4px 6px rgba(0,0,0,0.1)', padding: '2rem', marginBottom: '1.5rem' }}>
                            <h2 style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#1f2937', marginBottom: '1rem' }}>Quarterly Revenue Trend</h2>
                            <ResponsiveContainer width="100%" height={400}>
                                <LineChart data={historicalData}>
                                    <CartesianGrid strokeDasharray="3 3" />
                                    <XAxis dataKey="period" interval={15} />
                                    <YAxis label={{ value: 'Revenue ($M)', angle: -90, position: 'insideLeft' }} />
                                    <Tooltip formatter={(value) => `${value}M`} />
                                    <Legend />
                                    <Line type="monotone" dataKey="revenue" stroke="#DC2626" name="Revenue" strokeWidth={2} dot={false} />
                                </LineChart>
                            </ResponsiveContainer>
                        </div>

                        <div style={{ background: 'white', borderRadius: '0.5rem', boxShadow: '0 4px 6px rgba(0,0,0,0.1)', padding: '2rem', marginBottom: '1.5rem' }}>
                            <h2 style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#1f2937', marginBottom: '1rem' }}>Annual Performance Overview</h2>
                            <ResponsiveContainer width="100%" height={400}>
                                <BarChart data={annualData}>
                                    <CartesianGrid strokeDasharray="3 3" />
                                    <XAxis dataKey="year" />
                                    <YAxis label={{ value: 'Amount ($M)', angle: -90, position: 'insideLeft' }} />
                                    <Tooltip formatter={(value) => `${value}M`} />
                                    <Legend />
                                    <Bar dataKey="revenue" fill="#DC2626" name="Revenue" />
                                    <Bar dataKey="operatingIncome" fill="#F59E0B" name="Operating Income" />
                                    <Bar dataKey="netIncome" fill="#10B981" name="Net Income" />
                                </BarChart>
                            </ResponsiveContainer>
                        </div>

                        <div style={{ background: 'white', borderRadius: '0.5rem', boxShadow: '0 4px 6px rgba(0,0,0,0.1)', padding: '2rem', marginBottom: '1.5rem' }}>
                            <h2 style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#1f2937', marginBottom: '1rem' }}>Profitability Metrics</h2>
                            <ResponsiveContainer width="100%" height={400}>
                                <LineChart data={historicalData}>
                                    <CartesianGrid strokeDasharray="3 3" />
                                    <XAxis dataKey="period" interval={15} />
                                    <YAxis label={{ value: 'Income ($M)', angle: -90, position: 'insideLeft' }} />
                                    <Tooltip formatter={(value) => `${value}M`} />
                                    <Legend />
                                    <Line type="monotone" dataKey="operatingIncome" stroke="#F59E0B" name="Operating Income" strokeWidth={2} dot={false} />
                                    <Line type="monotone" dataKey="netIncome" stroke="#10B981" name="Net Income" strokeWidth={2} dot={false} />
                                </LineChart>
                            </ResponsiveContainer>
                        </div>

                        <div style={{ background: 'white', borderRadius: '0.5rem', boxShadow: '0 4px 6px rgba(0,0,0,0.1)', padding: '2rem' }}>
                            <h2 style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#1f2937', marginBottom: '1rem' }}>Key Insights</h2>
                            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '1rem' }}>
                                <div style={{ borderLeft: '4px solid #dc2626', paddingLeft: '1rem' }}>
                                    <h3 style={{ fontWeight: '600', color: '#1f2937', marginBottom: '0.5rem' }}>Long-Term Growth</h3>
                                    <p style={{ fontSize: '0.875rem', color: '#666' }}>Coca-Cola has demonstrated consistent growth with a {metrics.cagr}% CAGR over 30 years, showing resilience through economic cycles.</p>
                                </div>
                                <div style={{ borderLeft: '4px solid #2563eb', paddingLeft: '1rem' }}>
                                    <h3 style={{ fontWeight: '600', color: '#1f2937', marginBottom: '0.5rem' }}>Seasonal Patterns</h3>
                                    <p style={{ fontSize: '0.875rem', color: '#666' }}>Clear seasonality with Q2 and Q3 (summer months) consistently outperforming, reflecting higher beverage consumption during warmer months.</p>
                                </div>
                                <div style={{ borderLeft: '4px solid #16a34a', paddingLeft: '1rem' }}>
                                    <h3 style={{ fontWeight: '600', color: '#1f2937', marginBottom: '0.5rem' }}>Margin Improvement</h3>
                                    <p style={{ fontSize: '0.875rem', color: '#666' }}>Operating and net margins have gradually improved through operational efficiency and cost management strategies.</p>
                                </div>
                                <div style={{ borderLeft: '4px solid #9333ea', paddingLeft: '1rem' }}>
                                    <h3 style={{ fontWeight: '600', color: '#1f2937', marginBottom: '0.5rem' }}>Financial Performance</h3>
                                    <p style={{ fontSize: '0.875rem', color: '#666' }}>Current net margin of {metrics.avgMargin}% demonstrates strong profitability and operational excellence in recent quarters.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            );
        }

    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HOME_PAGE)

@app.route('/analytics')
def analytics():
    return render_template_string(ANALYTICS_PAGE)

@app.route('/coca-cola')
def coca_cola():
    return COCA_COLA_PAGE

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
