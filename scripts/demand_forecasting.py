import os
import pickle

import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

# ✅ Load dataset
data_path = os.path.join(os.path.dirname(__file__), "../data/cleaned_inventory_data.csv")
data = pd.read_csv(data_path)

# ✅ Detect sales column dynamically
sales_column = None
for col in data.columns:
    if "sales" in col.lower() or "sold" in col.lower() or "quantity" in col.lower():
        sales_column = col
        break

if sales_column is None:
    print("❌ ERROR: No sales column found. Please update dataset or script.")
    print("➡ Available columns:", list(data.columns))
    exit()

print(f"✅ Using sales column: {sales_column}")

# ✅ Ensure 'SKU' column exists
if "SKU" not in data.columns:
    print("❌ ERROR: 'SKU' column missing in dataset.")
    exit()

# ✅ Add a fake date index (since dataset lacks time series data)
data["Date"] = pd.date_range(start="2024-01-01", periods=len(data), freq="D")

# ✅ Aggregate sales per product over time
product_sales = data.groupby(["Date", "SKU"])[sales_column].sum().unstack()

# ✅ Ensure there is enough data for forecasting
if product_sales.shape[0] < 10 or product_sales.isna().sum().sum() > 0:
    print("⚠ WARNING: Not enough clean data points for ARIMA model. Skipping forecasting.")
    exit()

# ✅ Train ARIMA model for the first SKU
try:
    product_id = product_sales.columns[0]
    model = ARIMA(product_sales[product_id].dropna(), order=(5,1,0))
    model_fit = model.fit()

    # ✅ Save trained model
    model_path = os.path.join(os.path.dirname(__file__), "../models/demand_forecast_model.pkl")
    with open(model_path, "wb") as f:
        pickle.dump(model_fit, f)

    print(f"✅ Demand forecasting model trained and saved for SKU: {product_id}")
except Exception as e:
    print(f"❌ ERROR: ARIMA model training failed due to: {e}")
