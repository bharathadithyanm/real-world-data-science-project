import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("📊 Retail Sales Dashboard")

# Load dataset
df = pd.read_csv("data/retail_sales.csv")

# Show dataset
st.subheader("Dataset")
st.dataframe(df)

# Metrics
st.subheader("Business Metrics")

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

col1, col2 = st.columns(2)

col1.metric("Total Sales", f"₹{total_sales}")
col2.metric("Total Profit", f"₹{total_profit}")

# Sales by category
st.subheader("Sales by Category")

category_sales = df.groupby("Category")["Sales"].sum().reset_index()

fig = px.bar(
    category_sales,
    x="Category",
    y="Sales",
    color="Category",
    title="Category-wise Sales"
)

st.plotly_chart(fig)

# Profit chart
st.subheader("Profit Distribution")

fig2 = px.pie(
    df,
    names="Category",
    values="Profit",
    title="Profit by Category"
)

st.plotly_chart(fig2)