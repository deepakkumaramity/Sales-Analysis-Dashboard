import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os

# Load data
df = pd.read_csv('data/sales_data.csv')

# Dashboard title
st.title("Sales Analysis Dashboard")
st.markdown("<p style='text-align:center; color:gray;'>© Deepak Kumar</p>", unsafe_allow_html=True)

# Sidebar filters
products = st.sidebar.multiselect("Select Products", options=df['Product'].unique(), default=df['Product'].unique())
df_filtered = df[df['Product'].isin(products)]

# Total Revenue
total_revenue = df_filtered['Revenue'].sum()
st.metric("Total Revenue", f"₹{total_revenue}")

# Plot: Units Sold by Product
plt.figure(figsize=(8,5))
sns.barplot(x='Product', y='Units_Sold', data=df_filtered, ci=None)
plt.title("Units Sold by Product")
plt.text(0.5, -0.15, 'Deepak Kumar', fontsize=12, color='gray',
         ha='center', va='center', alpha=0.5, transform=plt.gca().transAxes)
plt.tight_layout()
plt.savefig('images/units_sold_by_product.png')
st.pyplot(plt)

# Plot: Revenue by Category
plt.figure(figsize=(8,5))
sns.barplot(x='Category', y='Revenue', data=df_filtered, ci=None)
plt.title("Revenue by Category")
plt.text(0.5, -0.15, 'Deepak Kumar', fontsize=12, color='gray',
         ha='center', va='center', alpha=0.5, transform=plt.gca().transAxes)
plt.tight_layout()
plt.savefig('images/revenue_by_category.png')
st.pyplot(plt)
