import streamlit as st
import pandas as pd
import plotly.express as px

# Page settings
st.set_page_config(page_title="Business Dashboard", layout="wide")

st.title("📊 Global Superstore Interactive Dashboard")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("superstore.csv", encoding='latin1')
    df['Order.Date'] = pd.to_datetime(df['Order.Date'])
    return df

df = load_data()

# ==============================
# SIDEBAR FILTERS
# ==============================

st.sidebar.header("🔎 Filter Data")

region = st.sidebar.multiselect(
    "Select Region",
    df["Region"].unique(),
    default=df["Region"].unique()
)

category = st.sidebar.multiselect(
    "Select Category",
    df["Category"].unique(),
    default=df["Category"].unique()
)

sub_category = st.sidebar.multiselect(
    "Select Sub-Category",
    df["Sub.Category"].unique(),
    default=df["Sub.Category"].unique()
)

# Apply filters
filtered_df = df[
    (df["Region"].isin(region)) &
    (df["Category"].isin(category)) &
    (df["Sub.Category"].isin(sub_category))
]

# If no data after filtering
if filtered_df.empty:
    st.warning("No data available for selected filters.")
else:

    # ==============================
    # KPIs
    # ==============================

    total_sales = filtered_df["Sales"].sum()
    total_profit = filtered_df["Profit"].sum()

    col1, col2 = st.columns(2)

    col1.metric("💰 Total Sales", f"${total_sales:,.2f}")
    col2.metric("📈 Total Profit", f"${total_profit:,.2f}")

    st.markdown("---")

    # ==============================
    # Sales by Region
    # ==============================

    st.subheader("Sales by Region")

    region_data = (
        filtered_df.groupby("Region")["Sales"]
        .sum()
        .reset_index()
    )

    fig_region = px.bar(
        region_data,
        x="Region",
        y="Sales",
        text_auto=True
    )

    st.plotly_chart(fig_region, use_container_width=True)

    # ==============================
    # Profit by Category
    # ==============================

    st.subheader("Profit by Category")

    category_data = (
        filtered_df.groupby("Category")["Profit"]
        .sum()
        .reset_index()
    )

    fig_category = px.pie(
        category_data,
        names="Category",
        values="Profit"
    )

    st.plotly_chart(fig_category, use_container_width=True)

    # ==============================
    # Top 5 Customers
    # ==============================

    st.subheader("🏆 Top 5 Customers by Sales")

    top_customers = (
        filtered_df.groupby("Customer.Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .reset_index()
    )

    fig_top = px.bar(
        top_customers,
        x="Customer.Name",
        y="Sales",
        text_auto=True
    )

    st.plotly_chart(fig_top, use_container_width=True)

    # ==============================
    # Show Raw Data
    # ==============================

    st.subheader("📄 Filtered Data Preview")
    st.dataframe(filtered_df.head(10))
