import pandas as pd
import sqlite3
import os

# === File Paths ===
RAW_DATA_DIR = "raw_data"
REPORTS_DIR = "reports"
WAREHOUSE_DIR = "warehouse"

DEVICES_FILE = os.path.join(RAW_DATA_DIR, "Devices.xlsx")
USERS_FILE = os.path.join(RAW_DATA_DIR, "Users.xlsx")
DB_PATH = os.path.join(WAREHOUSE_DIR, "AssetTracker.db")
REPORT_PATH = os.path.join(REPORTS_DIR, "Asset_Alerts_Report.xlsx")

# === Ensure directories exist ===
os.makedirs(REPORTS_DIR, exist_ok=True)
os.makedirs(WAREHOUSE_DIR, exist_ok=True)

# === Load Data ===
devices = pd.read_excel(DEVICES_FILE)
users = pd.read_excel(USERS_FILE)

# === Normalize Columns ===
devices.columns = devices.columns.str.strip().str.lower().str.replace(" ", "_")
users.columns = users.columns.str.strip().str.lower().str.replace(" ", "_")

# === Alert 1: Devices with no assigned user ===
missing_user_devices = devices[devices["assigned_to"].str.strip() == ""]

# === Alert 2: Devices marked Inactive or Missing ===
problematic_devices = devices[devices["status"].isin(["Inactive", "Missing"])]

# === Alert 3: Users with no assigned devices ===
assigned_emails = devices["assigned_to"].dropna().str.lower().str.strip().unique()
users["has_device"] = users["user_email"].str.lower().str.strip().isin(assigned_emails)
users_without_devices = users[~users["has_device"]]

# === Save Alerts Report (Excel) ===
with pd.ExcelWriter(REPORT_PATH) as writer:
    missing_user_devices.to_excel(writer, sheet_name="Devices Missing Users", index=False)
    problematic_devices.to_excel(writer, sheet_name="Inactive or Missing Devices", index=False)
    users_without_devices.to_excel(writer, sheet_name="Users Without Devices", index=False)

# === Save to SQLite ===
with sqlite3.connect(DB_PATH) as conn:
    devices.to_sql("devices", conn, if_exists="replace", index=False)
    users.to_sql("users", conn, if_exists="replace", index=False)
    missing_user_devices.to_sql("alert_missing_user", conn, if_exists="replace", index=False)
    problematic_devices.to_sql("alert_device_status", conn, if_exists="replace", index=False)
    users_without_devices.to_sql("alert_user_no_device", conn, if_exists="replace", index=False)

print(" ETL process complete. Alerts saved to Excel and SQLite.")
