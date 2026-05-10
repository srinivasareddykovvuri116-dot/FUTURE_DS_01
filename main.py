import pandas as pd
import matplotlib.pyplot as pl
import seaborn as sns




df = pd.read_csv("data/sales_data_sample.csv", encoding="latin1")



print(df.head())

totalsales=df["SALES"].sum()
print("\nTotal Sales:", totalsales)

#grouping of products and sales
top_products = df.groupby("PRODUCTLINE")["SALES"].sum().sort_values(ascending=False)
print("\nTop Products:", top_products)


#graph of total sales
top_products.plot(kind="bar")
pl.title("Top Product Sales")
pl.xlabel("PRODUCTLINE")
pl.ylabel("SALES")
pl.tight_layout()
pl.savefig("images/top_products.png")
pl.show()

#group of country and sales
country_sales=df.groupby("COUNTRY")["SALES"].sum().sort_values(ascending=False)
print("\nSales By Country: ", country_sales)

#graph of country sales
country_sales.plot(kind="bar", figsize=(12,6))
pl.title("Sales By Country")
pl.xlabel("COUNTRY")
pl.ylabel("SALES")
pl.tight_layout()
pl.savefig("images/country_sales.png")
pl.show()


#total slaes for each month 
monthly_sales=df.groupby("MONTH_ID")["SALES"].sum()
print("\nMOnthly Sales:", monthly_sales)

# monthly sales graph
monthly_sales.plot(kind="line", marker="o", figsize=(10,5))
pl.title("Monthly Sales Trend")
pl.xlabel("MONTH")
pl.ylabel("SALES")
pl.grid(True)
pl.tight_layout()
pl.savefig("images/monthly_sales.png")
pl.show()

#top customer and sales group
top_customers=df.groupby("CUSTOMERNAME")["SALES"].sum().sort_values(ascending=False)
print("\nTop Customers:", top_customers.head(10))

#graph for top 10 customers
top_customers.head(10).plot(kind="bar", figsize=(15,7.5))
pl.title("Top 10 Customers")
pl.xlabel("CUSTOMERS")
pl.ylabel("SALES")
pl.tight_layout()
pl.savefig("images/top_customers.png")
pl.show()




# KPI Metrics

total_sales = df["SALES"].sum()

total_orders = df["ORDERNUMBER"].nunique()

total_customers = df["CUSTOMERNAME"].nunique()

average_sales = df["SALES"].mean()

total_product_categories = df["PRODUCTLINE"].nunique()

print("\n KPI Metrics")

print("Total Sales: ", round(total_sales, 2))

print("Total Orders: ", total_orders)

print("Total Customers: ", total_customers)

print("Average Sales Per Order: ", round(average_sales, 2))

print("Total Product Categories: ", total_product_categories)

#BEST year analysis 
yearly_sales= df.groupby("YEAR_ID")["SALES"].sum()
print(yearly_sales)

#graph of yearly sales
yearly_sales.plot(kind="line", marker="o", figsize=(10,5))

pl.title("Yearly Sales Performance")
pl.xlabel("YEAR_ID")
pl.ylabel("SALES")
pl.grid(True)
pl.tight_layout()
pl.savefig("images/yearly_sales.png")
pl.show()

#deal size 

deal_size_sales= df.groupby("DEALSIZE")["SALES"].sum().sort_values(ascending=False)

# Plot deal size sales
deal_size_sales.plot(kind="bar", figsize=(8,5))
pl.title("Sales By Deal Size")
pl.xlabel("Deal Size")
pl.ylabel("Sales")
pl.tight_layout()
pl.savefig("images/deal_size_sales.png")
pl.show()



# =========================================
# HEATMAP ANALYSIS
# =========================================

pl.figure(figsize=(10,6))

sns.heatmap(
    df.select_dtypes(include='number').corr(),
    annot=True,
    cmap="coolwarm"
)

pl.title("Correlation Heatmap")

pl.tight_layout()

pl.savefig("images/correlation_heatmap.png")

pl.show()



# =========================================
# STACKED BAR CHART
# =========================================

stacked_data = df.pivot_table(
    values="SALES",
    index="YEAR_ID",
    columns="PRODUCTLINE",
    aggfunc="sum"
)

stacked_data.plot(
    kind="bar",
    stacked=True,
    figsize=(12,6)
)

pl.title("Yearly Product Sales by Category")

pl.xlabel("YEAR_ID")

pl.ylabel("SALES")

pl.tight_layout()

pl.savefig("images/stacked_sales_chart.png")

pl.show()



print("\nAdvanced Visualizations Added Successfully. ")

