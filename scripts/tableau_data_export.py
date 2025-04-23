import os

import pandas as pd

# ✅ Load optimized inventory data
data_path = os.path.join(os.path.dirname(__file__), "../data/optimized_inventory.csv")
data = pd.read_csv(data_path)

# ✅ Ensure the reports directory exists
reports_dir = os.path.join(os.path.dirname(__file__), "../reports")
if not os.path.exists(reports_dir):
    os.makedirs(reports_dir)
    print(f"✅ Created missing directory: {reports_dir}")

# ✅ Save cleaned dataset for Tableau
tableau_file_path = os.path.join(reports_dir, "inventory_dashboard_data.csv")
data.to_csv(tableau_file_path, index=False)

print(f"✅ Data exported for Tableau visualization: {tableau_file_path}")
