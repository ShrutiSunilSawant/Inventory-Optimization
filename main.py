import os

# Ensure scripts are executed from the correct directory
script_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scripts")

print("🚀 Running Inventory Optimization Analysis...")

os.system(f"python {script_dir}/data_preprocessing.py")
os.system(f"python {script_dir}/demand_forecasting.py")
os.system(f"python {script_dir}/inventory_optimization.py")
os.system(f"python {script_dir}/tableau_data_export.py")

print("✅ Inventory Analysis Completed! Ready for Tableau Dashboard.")
