 # E-Commerce Sales Analytics

 ## 🚀 Live Dashboard

👉 [View the Interactive E-Commerce Sales Analytics Dashboard](https://ecommerce-sales-analytics-hzfktactjevdon9atbh8ch.streamlit.app/)

A Python-based e-commerce analytics project that transforms raw transactional data into actionable business insights through data cleaning, feature engineering, customer segmentation, product analysis, return analysis, and an interactive Streamlit dashboard.

## 📊 Project Overview

This project analyzes the **Online Retail II** dataset to understand:

- Overall sales and revenue performance
- Product-level sales and revenue contribution
- Customer purchasing behavior
- RFM-based customer segmentation
- Return and cancellation patterns
- Country-level market performance
- Sales patterns by time and hour
- International market opportunities

The project combines exploratory data analysis with business-focused analytics and presents the final insights through an interactive Streamlit dashboard.

## 🎯 Business Questions

The analysis focuses on questions such as:

- Which products generate the most revenue?
- Which countries contribute the most sales?
- When does the business generate the highest sales?
- Which customer segments contribute the most revenue?
- Which products and countries have significant return activity?
- How do product sales volume and revenue relate to each other?
- Which international markets show higher average order values?

## 🛠️ Technologies Used

- Python
- Pandas
- Jupyter Notebook
- Streamlit
- OpenPyXL
- Git & GitHub

## 📈 Key Analyses

### Sales Performance
- Monthly revenue trends
- Total revenue and units sold
- Order-level performance
- Sales by hour

### Product Analytics
- Top products by revenue
- Product sales volume
- Product volume vs revenue relationship
- Product performance segmentation

### Customer Analytics
- Customer-level metrics
- RFM analysis
- Customer segmentation
- Revenue contribution by segment

### Market Analytics
- Country-level revenue
- Order volume by country
- Average order value
- International market comparison

### Return Analytics
- Returned units
- Return value
- Return rate
- Product-level return analysis
- Country-level return analysis
- Cancellation-based return analysis

## 🔎 Data Quality & Methodology

The dataset contains normal sales transactions as well as cancellations, returns, adjustments, damaged goods, and other non-standard transaction descriptions.

The analysis therefore includes dedicated data-cleaning and validation steps before calculating business metrics.

Revenue is calculated using:

`SalesValue = Quantity × Price`

Positive-quantity transactions are treated as sales for the primary sales-performance analysis, while negative-quantity transactions are separately analyzed as recorded returns or adjustments.

Customer segmentation is based on validated RFM analysis.

## 📊 Interactive Dashboard

The project includes a Streamlit dashboard containing:

- KPI cards
- Monthly revenue trend
- Top products by revenue
- Top countries by revenue
- Product volume vs revenue analysis
- RFM customer segmentation
- Return impact analysis
- Sales revenue by hour
- International market analysis
- Data quality and methodology notes

## 📁 Project Structure

```text
Ecommerce-Sales-Analytics/
│
├── dashboard/
│   └── app.py
│
├── sales_analysis.ipynb
├── online_retail_II.xlsx
├── requirements.txt
├── .gitignore
└── README.md