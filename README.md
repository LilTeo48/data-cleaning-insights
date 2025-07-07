# Data Cleaning & Insights Report

This project demonstrates how to take a messy dataset and transform it into clean, structured data using Python and Pandas. It includes basic feature engineering, data cleanup, and a visualization to gain actionable insights from a fictional product sales dataset.

---

# Overview

- Cleans a CSV file with inconsistent date formats, missing values, and duplicates.
- Converts column types and formats.
- Groups and visualizes revenue by product.
- Stores cleaned data and plots for further use.

---

# Technologies Used

- Python 3.9+
- Pandas
- Matplotlib
- PyCharm (for development)

---

# Project Structure

data-cleaning-insights/
├── data/
│ └── raw_data.csv # Original messy dataset
├── cleaned_data/
│ └── cleaned_data.csv # Cleaned version
├── visuals/
│ └── revenue_by_product.png # Bar chart visualization
├── data_analysis.py # Main Python script
└── README.md

---

# How to Run 

1. Clone the repo:
  
   git clone https://github.com/LilTeo48/data-cleaning-insights.git
   cd data-cleaning-insights
Install dependencies:

pip install pandas matplotlib
Run the script:

python data_analysis.py
Output:

Cleaned data: cleaned_data/cleaned_data.csv

Plot: visuals/revenue_by_product.png
