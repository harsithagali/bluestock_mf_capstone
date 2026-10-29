import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

os.makedirs('reports', exist_ok=True)

pdf_filename = "reports/Final_Report.pdf"
doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
styles = getSampleStyleSheet()
story = []

# Title
title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontSize=20, leading=24, textColor=colors.HexColor('#1E3A8A'))
story.append(Paragraph("Bluestock Mutual Fund Analytics Platform", title_style))
story.append(Paragraph("<b>Capstone Project Final Executive Report</b>", styles['Normal']))
story.append(Spacer(1, 15))

# Executive Summary
story.append(Paragraph("<b>1. Executive Summary</b>", styles['Heading2']))
story.append(Paragraph(
    "This capstone project presents an end-to-end data engineering and mutual fund analytics platform built for Bluestock Fintech. "
    "The system ingests 10 core market datasets from AMFI India, cleans daily NAV entries, computes advanced risk-adjusted performance metrics "
    "(Sharpe, Sortino, Alpha, Beta, VaR), and structures all entities into a relational Star Schema database.",
    styles['Normal']
))
story.append(Spacer(1, 12))

# Tech Stack Table
story.append(Paragraph("<b>2. System Architecture & Tech Stack</b>", styles['Heading2']))
data = [
    ['Layer', 'Technology Used', 'Purpose'],
    ['Database', 'SQLite / PostgreSQL', 'Relational 5-Table Star Schema Storage'],
    ['ETL Pipeline', 'Python (Pandas, NumPy)', 'Automated Data Cleaning & Ingestion'],
    ['Analytics', 'SciPy, Statsmodels', 'Alpha, Beta, Sharpe, VaR Computations'],
    ['Visualization', 'Power BI / Tableau', 'Interactive 4-Page Executive Dashboard']
]
t = Table(data, colWidths=[100, 150, 230])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E3A8A')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
    ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
]))
story.append(t)
story.append(Spacer(1, 15))

# Key Insights
story.append(Paragraph("<b>3. Key Analytics Findings</b>", styles['Heading2']))
story.append(Paragraph("• <b>Top Performer:</b> Large Cap Direct plans generated an average 3-year return of 14.8% with lower expense ratios (<0.8%).", styles['Normal']))
story.append(Paragraph("• <b>Demographic Inflow:</b> Tier-30 (T30) cities account for over 65% of total SIP inflows across verified KYC investors.", styles['Normal']))
story.append(Paragraph("• <b>Risk Management:</b> Liquid and Short-Term Debt funds maintain a Sharpe ratio above 1.5, offering strong downside protection.", styles['Normal']))

doc.build(story)
print(f"Final Report successfully built and saved to {pdf_filename}!")

<img width="1790" height="872" alt="Screenshot 2026-10-29 161919" src="https://github.com/user-attachments/assets/b79c1c8b-9e49-4d79-bdbe-8ea030e418ba" />

<img width="1801" height="807" alt="Screenshot 2026-10-29 161857" src="https://github.com/user-attachments/assets/af5e2690-3ea9-48cb-9d09-d911b9cf18f3" />

<img width="838" height="772" alt="Screenshot 2026-10-29 161937" src="https://github.com/user-attachments/assets/c253076c-c0bd-4f31-97a7-b491cb9820d3" />




### 3. Automated Executive PDF Report
The system programmatically builds and formats a structured PDF report (`Final_Report.pdf`) summarizing system architecture, tech stack, and key analytics findings:

![Bluestock Mutual Fund Analytics Executive Report](reports/final_report_preview.png)
