import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load cleaned data
data = pd.read_csv("../data/cleaned_inventory_data.csv")

# Sales trend visualization
plt.figure(figsize=(12, 6))
sns.lineplot(data=data, x="Date", y="Sales_Quantity", hue="Category")
plt.title("Sales Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Sales Quantity")
plt.xticks(rotation=45)
plt.grid()
plt.show()

# Inventory levels
plt.figure(figsize=(10, 5))
sns.barplot(data=data, x="Product_ID", y="Stock_Level", palette="viridis")
plt.title("Current Stock Levels")
plt.xlabel("Product ID")
plt.ylabel("Stock Level")
plt.xticks(rotation=45)
plt.show()
