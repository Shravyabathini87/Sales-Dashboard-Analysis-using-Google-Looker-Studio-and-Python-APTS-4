import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("C:\\Users\\Shravya\\OneDrive - Malla Reddy Engineering College for Women\\Desktop\\apexxx\\TASK 4\\dataset.csv")

# Display basic information
print("Dataset Overview")
print(data.head())

# Total Sales
total_sales = data["Sales"].sum()
print("Total Sales:", total_sales)

# Total Profit
total_profit = data["Profit"].sum()
print("Total Profit:", total_profit)

# Sales by Region
region_sales = data.groupby("Region")["Sales"].sum()
print("\nSales by Region")
print(region_sales)

# Profit by Category
category_profit = data.groupby("Category")["Profit"].sum()
print("\nProfit by Category")
print(category_profit)

# Visualization: Sales by Region
region_sales.plot(kind="bar", title="Sales by Region")
plt.ylabel("Sales")
plt.show()

# Visualization: Profit by Category
category_profit.plot(kind="bar", title="Profit by Category")
plt.ylabel("Profit")
plt.show()