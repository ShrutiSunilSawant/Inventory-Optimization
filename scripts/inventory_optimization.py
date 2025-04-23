import os

import pandas as pd

# ✅ Correct file path handling
data_path = os.path.join(os.path.dirname(__file__), "../data/cleaned_inventory_data.csv")
data = pd.read_csv(data_path)

# ✅ Detect correct stock level column
stock_column = None
for col in data.columns:
    if "stock" in col.lower() or "inventory" in col.lower():
        stock_column = col
        break

if stock_column is None:
    print("❌ ERROR: No stock column found. Please update dataset or script.")
    print("➡ Available columns:", list(data.columns))
    exit()

print(f"✅ Using stock column: {stock_column}")

# ✅ Detect reorder point column (or estimate it)
reorder_column = "Reorder_Point"
if reorder_column not in data.columns:
    print("⚠ Reorder point column missing! Computing estimated reorder points.")
    data[reorder_column] = data[stock_column] * 0.3  # Assuming 30% threshold

# ✅ Compute Economic Order Quantity (EOQ)
def calculate_eoq(demand, order_cost=50, holding_cost=5):
    return ((2 * demand * order_cost) / holding_cost) ** 0.5

demand_column = "Number of products sold"
if demand_column not in data.columns:
    print("❌ ERROR: Demand column missing. Please check dataset.")
    exit()

data["EOQ"] = data[demand_column].apply(lambda x: calculate_eoq(x))

# ✅ Save optimized inventory data
optimized_file_path = os.path.join(os.path.dirname(__file__), "../data/optimized_inventory.csv")
data.to_csv(optimized_file_path, index=False)

print(f"✅ Inventory optimization completed! Data saved as: {optimized_file_path}")
