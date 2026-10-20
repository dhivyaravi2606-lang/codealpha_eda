# CodeAlpha Task 2 — Retail Sales Data Analysis (EDA)

## Project overview
This beginner-friendly project explores a sample retail sales dataset using Python. It checks dataset structure, missing values, duplicate rows, numerical summaries, sales by product/category/region, payment methods, and daily sales trends.

**Dataset note:** `data/retail_sales.csv` is a synthetic practice dataset created for learning. It is not real customer or company data.

## Tools
Python, Pandas, Matplotlib, Seaborn, CSV.

## Folder structure
- `data/retail_sales.csv` — sample sales dataset (150 records)
- `eda.py` — analysis and chart-generation code
- `requirements.txt` — required Python libraries
- `output/` — generated charts, analysed CSV, and summary after running

## Run in VS Code
1. Extract the ZIP file.
2. Open the `CodeAlpha_EDA` folder in VS Code.
3. Select **Terminal → New Terminal**.
4. Install libraries: `pip install -r requirements.txt`
5. Run: `python eda.py`
6. Open the `output` folder to see the results.

## Outputs
- `sales_by_product.png`
- `sales_by_category.png`
- `sales_by_region.png`
- `daily_sales_trend.png`
- `retail_sales_cleaned.csv`
- `eda_summary.txt`

## What you learn
- Loading CSV files with Pandas
- Checking rows, columns, data types, missing values, and duplicates
- Calculating summary statistics
- Comparing sales by product, category, and region
- Creating charts to communicate findings
