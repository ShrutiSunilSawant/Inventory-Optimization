# Inventory-Optimization

📦 Inventory Optimization

This project leverages data analytics and time-series forecasting techniques to analyze and optimize inventory levels. The goal is to ensure that the right products are available at the right time—minimizing stockouts and excess inventory.

## 📌 Table of Contents
- Overview
- Features
- Project Structure
- Installation
- Usage
- Data Sources
- Future Enhancements

## 🚀 Overview

In today's fast-paced retail and supply chain environments, managing inventory effectively is crucial. This project provides a comprehensive pipeline that:
- **Preprocesses raw data**: Cleans and formats inventory and sales data.
- **Forecasts demand**: Uses an ARIMA model to predict future sales (if enough time-series data is available).
- **Optimizes inventory**: Calculates key metrics such as Economic Order Quantity (EOQ) and estimated reorder points.
- **Prepares data for visualization**: Exports data to a CSV file, ready for creating interactive dashboards in Tableau.

## ✅ Features

### **Data Preprocessing**
- Loads datasets from the `data/` folder.
- Handles missing values and converts date columns (if available).
- Saves a cleaned version of the dataset.

### **Demand Forecasting**
- Detects the appropriate sales column dynamically.
- Applies an ARIMA model to forecast demand for each product SKU.
- Skips forecasting gracefully if there is insufficient data.

### **Inventory Optimization**
- Detects stock level information.
- Computes Economic Order Quantity (EOQ).
- Estimates reorder points when such data is missing.

### **Tableau Data Export**
- Exports the optimized dataset to a CSV file for visualization in Tableau.
- Automatically creates the output directory if it does not exist.

## 📂 Project Structure

```
inventory_optimization_project/
│
├── data/
│   ├── supply_chain_dataset.csv
│   ├── inventory_management_data.csv
│   ├── supply_chain_analysis.csv
│   ├── cleaned_inventory_data.csv
│   └── optimized_inventory.csv
│
├── reports/
│   └── inventory_dashboard_data.csv
│
├── scripts/
│   ├── data_preprocessing.py
│   ├── demand_forecasting.py
│   ├── eda_visualization.py
│   ├── inventory_optimization.py
│   ├── reorder_alerts.py
│   └── tableau_data_export.py
│
├── main.py
├── requirements.txt
└── README.md
```

## 🛠 Installation

### **Install dependencies**

Ensure you have Python installed (preferably Python 3.8 or higher). Then run:

```bash
pip install -r requirements.txt
```

The required libraries are:
- `pandas`
- `numpy`
- `statsmodels`
- `scipy`
- `pickle-mixin`

### **Place your dataset(s) in the `data/` folder.**

## ▶️ Usage

### **Run the full pipeline**

Execute the main script to run all stages sequentially:

```bash
python main.py
```

The pipeline performs:
- Data preprocessing
- Demand forecasting (if enough data is available)
- Inventory optimization
- Data export for Tableau

### 🔄 Model File

The ARIMA demand forecasting model (`demand_forecast_model.pkl`) is not included in this repository.  
It will be **automatically created** and saved to the `/models/` folder when you run:

```bash
python scripts/demand_forecasting.py
```

### **View the Tableau Dashboard**

1. Open the generated CSV file at `reports/inventory_dashboard_data.csv` in Tableau.
2. Create visualizations such as:
   - Sales Trends 📈
   - Stock vs. Reorder Levels 📊
   - Pricing vs. Demand Scatter Plot ⚡

## 📊 Data Sources

This project supports multiple datasets. Place one or more of the following files in the `data/` folder:
- `supply_chain_dataset.csv`
- `inventory_management_data.csv`
- `supply_chain_analysis.csv`

The script automatically selects the first available dataset.

## 🔮 Future Enhancements

- **Improve Forecasting:** Enhance the ARIMA model or explore alternative models (e.g., LSTM) for better demand forecasting.
- **Real-time Data Integration:** Connect to a live database for real-time inventory monitoring.
- **Web Dashboard:** Develop a Flask or Django web application for interactive inventory management.

---

💡 **Feel free to contribute, suggest improvements, or reach out for any questions!**

🚀 Happy Analyzing! 🎯
