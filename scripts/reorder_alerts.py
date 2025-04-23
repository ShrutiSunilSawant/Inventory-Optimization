import pandas as pd

# Load optimized inventory data
inventory_data = pd.read_csv("../data/optimized_inventory.csv")

# Check for low stock
low_stock_items = inventory_data[inventory_data["Stock_Level"] <= inventory_data["Reorder_Point"]]

if not low_stock_items.empty:
    print("🚨 Reorder Alerts:")
    print(low_stock_items[["Product_ID", "Stock_Level", "Reorder_Point"]])
else:
    print("✅ All stocks are at safe levels!")
