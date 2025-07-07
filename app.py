import streamlit as st
import pandas as pd
import sqlite3

#Load data from SQLite
DB_PATH = "AssetTracker.db"

def load_table(table_name):
    with sqlite3.connect(DB_PATH) as conn:
        return pd.read_sql(f"SELECT * FROM {table_name}", conn)

#UI setup
st.set_page_config(page_title="IT Asset Tracker", layout="wide")
st.title("IT Asset Tracker & Alert Dashboard")

#Sidebar filters
st.sidebar.header("Filters")
status_filter = st.sidebar.multiselect("Filter by Device Status", ["Active", "Inactive", "Missing"])

#Load Data
devices = load_table("devices")
users = load_table("users")
alert_missing_user = load_table("alert_missing_user")
alert_device_status = load_table("alert_device_status")
alert_user_no_device = load_table("alert_user_no_device")

#Filtered Devices Table
if status_filter:
    filtered_devices = devices[devices["Status"].isin(status_filter)]
else:
    filtered_devices = devices

st.subheader("Devices")
st.dataframe(filtered_devices, use_container_width=True)

#Alerts Section
st.markdown("---")
st.subheader("Alerts")

col1, col2, col3 = st.columns(3)
col1.metric("Devices Missing Users", len(alert_missing_user))
col2.metric("Inactive or Missing Devices", len(alert_device_status))
col3.metric("Users Without Devices", len(alert_user_no_device))

with st.expander("Devices Missing Assigned Users"):
    st.dataframe(alert_missing_user, use_container_width=True)

with st.expander("Inactive or Missing Devices"):
    st.dataframe(alert_device_status, use_container_width=True)

with st.expander("Users without Assigned Devices"):
    st.dataframe(alert_user_no_device, use_container_width=True)

st.markdown("---")
st.caption("Built by Tyler Chadwick | GitHub: [@LilTeo48] ](https://github.com/LilTeo48)")