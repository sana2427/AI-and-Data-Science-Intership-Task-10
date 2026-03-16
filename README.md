# Task 5: Interactive Business Dashboard in Streamlit

---

## Overview
This repository contains the solution for Task 5: Interactive Business Dashboard, completed as part of my AI & Data Science Internship tasks.  
The task focuses on building an interactive dashboard to analyze sales, profit, and customer performance using the Global Superstore dataset.

---

## Objective
The objective of this task is to develop an interactive Business Intelligence (BI) dashboard that allows dynamic exploration of sales data.  
Users can filter by region, category, and sub-category, visualize key performance indicators (KPIs), and identify top customers to gain actionable business insights.

---

## Dataset
**Dataset Name:** Global Superstore Dataset  
**Type:** Structured CSV dataset  

---

### Dataset Description
- **Total Records:** ~50,000 (depends on version)  
- **Target Metrics:** Sales, Profit, Top Customers  

### **Features:**
  - Order Date
  - Region
  - Category
  - Sub-Category
  - Sales
  - Profit
  - Customer Name  

The Global Superstore dataset contains sales transactions from multiple regions, categories, and customers, enabling detailed analysis of business performance.

---

## Tools & Technologies Used
- Python  
- pandas  
- Plotly  
- Streamlit  
- Jupyter Notebook / Google Colab  

---

## Approach

### 1️⃣ Data Loading
- Loaded the dataset using `pandas.read_csv()`  
- Converted CSV data into a pandas DataFrame for easy manipulation  

### 2️⃣ Data Inspection
- Used the following pandas functions:
  - `.shape` → to check dataset dimensions  
  - `.info()` → to inspect data types and missing values  
  - `.columns` → to view column names  
  - `.head()` → to preview initial rows  

### 3️⃣ Data Cleaning & Preprocessing
- Checked for missing values using `.isnull().sum()`  
- Renamed columns to avoid spaces/dots for smooth plotting  
- Removed duplicates using `.duplicated()` and `.drop_duplicates()`  
- Converted `Order Date` to datetime for analysis  

### 4️⃣ Exploratory Data Analysis (EDA)
- Calculated total sales and profit  
- Analyzed top 5 customers by sales  
- Examined sales and profit by region, category, and sub-category  

### 5️⃣ Streamlit Dashboard
- Built interactive filters in sidebar:
  - Region  
  - Category  
  - Sub-Category  
- Displayed KPIs:
  - Total Sales  
  - Total Profit  
  - Top 5 Customers  
- Visualizations:
  - Bar chart for Sales by Region  
  - Pie chart for Profit by Category  
  - Bar chart for Top 5 Customers by Sales  
- Added data table preview of filtered dataset  
- Users can interact with filters and visualize KPIs dynamically

### 6️⃣ Dashboard Deployment
- Ran dashboard locally using:
```bash
pip install streamlit pandas plotly
streamlit run app.py
```

---

## Dashboard Live Preview
```bash
https://ai-and-data-science-intership-task-10-cpsozr2gy8fnzadzkxgm4q.streamlit.app/
```


---

## Results & Insights

- Certain regions contribute significantly higher sales, indicating strong market demand
- Some categories generate high sales but lower profits, highlighting areas for cost optimization
- A small group of customers contributes a large portion of total sales
- Interactive filters allow quick analysis and comparison of sales trends

---

## Conclusion

This task successfully demonstrates the creation of an interactive business dashboard.
The Global Superstore dataset was effectively cleaned, analyzed, and visualized to provide meaningful insights.
The dashboard allows stakeholders to make data-driven decisions efficiently and supports better business strategy planning.

---

## Skills Gained

- Business Intelligence (BI) dashboarding
- Data cleaning and preprocessing
- Interactive visualization with Streamlit
- KPI analysis and data storytelling
- Dynamic filtering and user interactivity

