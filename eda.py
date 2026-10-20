from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# CodeAlpha Task 2: Exploratory Data Analysis (EDA)
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "retail_sales.csv"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

def main():
    if not DATA_PATH.exists():
        print(f"Dataset not found: {DATA_PATH}")
        return

    df = pd.read_csv(DATA_PATH)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    for col in ["quantity", "unit_price", "total_sales"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    print("\n========== RETAIL SALES EDA ==========")
    print(f"Rows: {df.shape[0]} | Columns: {df.shape[1]}")
    print("\nFirst 5 rows:\n", df.head().to_string(index=False))
    print("\nColumn information:")
    df.info()
    print("\nMissing values:\n", df.isnull().sum())
    print("\nDuplicate rows:", df.duplicated().sum())
    print("\nNumerical summary:\n", df[["quantity", "unit_price", "total_sales"]].describe().round(2))

    total_revenue = df["total_sales"].sum()
    total_orders = df["order_id"].nunique()
    total_units = df["quantity"].sum()
    average_order_value = df.groupby("order_id")["total_sales"].sum().mean()
    product_sales = df.groupby("product")["total_sales"].sum().sort_values(ascending=False)
    category_sales = df.groupby("category")["total_sales"].sum().sort_values(ascending=False)
    region_sales = df.groupby("region")["total_sales"].sum().sort_values(ascending=False)

    print("\n========== KEY FINDINGS ==========")
    print(f"Total sales revenue: Rs. {total_revenue:,.2f}")
    print(f"Number of orders: {total_orders}")
    print(f"Total units sold: {total_units}")
    print(f"Average order value: Rs. {average_order_value:,.2f}")
    print("\nSales by product:\n", product_sales.round(2).to_string())
    print("\nSales by category:\n", category_sales.round(2).to_string())
    print("\nSales by region:\n", region_sales.round(2).to_string())
    print("\nPayment methods:\n", df["payment_method"].value_counts().to_string())

    plt.figure(figsize=(10, 6))
    product_sales.sort_values().plot(kind="barh")
    plt.title("Total Sales by Product")
    plt.xlabel("Total Sales (INR)")
    plt.ylabel("Product")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "sales_by_product.png", dpi=150)
    plt.close()

    plt.figure(figsize=(8, 5))
    category_sales.plot(kind="bar")
    plt.title("Total Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Sales (INR)")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "sales_by_category.png", dpi=150)
    plt.close()

    plt.figure(figsize=(8, 5))
    region_sales.plot(kind="bar")
    plt.title("Total Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Total Sales (INR)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "sales_by_region.png", dpi=150)
    plt.close()

    daily_sales = df.groupby(df["date"].dt.date)["total_sales"].sum().sort_index()
    plt.figure(figsize=(10, 5))
    daily_sales.plot()
    plt.title("Daily Sales Trend")
    plt.xlabel("Date")
    plt.ylabel("Total Sales (INR)")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "daily_sales_trend.png", dpi=150)
    plt.close()

    df.to_csv(OUTPUT_DIR / "retail_sales_cleaned.csv", index=False)
    summary = [
        "RETAIL SALES EDA - KEY FINDINGS", "===============================",
        f"Rows analysed: {len(df)}", f"Columns: {len(df.columns)}",
        f"Missing values total: {int(df.isnull().sum().sum())}",
        f"Duplicate rows: {int(df.duplicated().sum())}",
        f"Total sales revenue: Rs. {total_revenue:,.2f}",
        f"Number of orders: {total_orders}", f"Total units sold: {total_units}",
        f"Average order value: Rs. {average_order_value:,.2f}", "",
        f"Top product by sales: {product_sales.index[0]} - Rs. {product_sales.iloc[0]:,.2f}",
        f"Top category by sales: {category_sales.index[0]} - Rs. {category_sales.iloc[0]:,.2f}",
        f"Top region by sales: {region_sales.index[0]} - Rs. {region_sales.iloc[0]:,.2f}",
        "", "Note: Synthetic sample dataset created for learning and demonstration."
    ]
    (OUTPUT_DIR / "eda_summary.txt").write_text("\n".join(summary), encoding="utf-8")
    print(f"\nEDA complete! Check the output folder: {OUTPUT_DIR}")
    print("Charts created: sales_by_product.png, sales_by_category.png, sales_by_region.png, daily_sales_trend.png")

if __name__ == "__main__":
    main()
