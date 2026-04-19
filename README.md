# Retail Data Pipeline & Analysis

## Overview
This project implements a basic ETL (Extract, Transform, Load) pipeline on a retail sales dataset.  
The goal is to clean raw data, store it in a MySQL database, and perform analysis using SQL and Python.

---

## Project Structure

retail-data-pipeline/
│
├── data/
│ └── raw/
│ └── SampleSuperstore.csv
│
├── scripts/
│ ├── extract.py
│ ├── transform.py
│ ├── load.py
│
├── notebooks/
│ └── eda.ipynb
│
├── pipeline.py
├── requirements.txt
└── README.md


---

## Workflow

### 1. Extract
- Load raw CSV data into a Pandas DataFrame

### 2. Transform
- Clean column names  
- Remove duplicates and null values  
- Convert data types  
- Create new column: `profit_margin`

### 3. Load
- Store processed data into MySQL using SQLAlchemy  

---

## Analysis

### SQL (MySQL)
- Region-wise total sales  
- Category-wise total profit  
- Top cities by sales  
- Average discount by segment  
- Ranking cities within regions using window functions  

### EDA (Python)
- Sales distribution across regions  
- Profit by category  
- Relationship between discount and profit  

---

## Tech Stack
- Python  
- Pandas  
- MySQL  
- SQLAlchemy  
- Matplotlib  

---

## How to Run

1. Install dependencies:

pip install -r requirements.txt


2. Run the pipeline:

python pipeline.py


3. Verify in MySQL:
```sql
SELECT * FROM orders LIMIT 5;
