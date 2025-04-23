import os

import pandas as pd

# ✅ Ensure correct data folder path
data_dir = os.path.join(os.path.dirname(__file__), "../data")

# ✅ Define dataset file names
dataset_files = [
    "supply_chain_dataset.csv",
    "inventory_management_data.csv",
    "supply_chain_analysis.csv"
]

# ✅ Find the first available dataset
dataset_path = None
for file in dataset_files:
    full_path = os.path.join(data_dir, file)
    if os.path.exists(full_path):
        dataset_path = full_path
        break

# ✅ If no dataset is found, exit with error
if dataset_path is None:
    print(f"❌ ERROR: No dataset found in '{data_dir}'.")
    print("➡ Ensure a valid dataset file exists in the 'data/' folder.")
    exit()

print(f"✅ Using dataset: {dataset_path}")

# ✅ Load dataset
data = pd.read_csv(dataset_path)

# ✅ Preview dataset
print("\n🔍 Preview of the dataset:")
print(data.head())

# ✅ Drop missing values (if any)
data.dropna(inplace=True)

# ✅ Convert date columns (if applicable)
date_columns = ["Date", "Order Date", "Delivery Date", "Sales Date"]
for col in date_columns:
    if col in data.columns:
        data[col] = pd.to_datetime(data[col], errors="coerce")
        print(f"📅 Converted column '{col}' to datetime format.")

# ✅ Save cleaned dataset
cleaned_file_path = os.path.join(data_dir, "cleaned_inventory_data.csv")
data.to_csv(cleaned_file_path, index=False)

print(f"\n✅ Data preprocessing completed! Cleaned data saved as: {cleaned_file_path}")
