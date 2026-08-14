import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="E-Commerce Sales Analytics",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Load Dataset
# -----------------------------

df = pd.read_excel("online_retail_II.xlsx")

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# -----------------------------
# Dashboard Header
# -----------------------------

# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.title("📊 Dashboard")

st.sidebar.markdown(
    """
    **E-Commerce Sales Analytics**

    Use this dashboard to explore:

    - Sales performance
    - Product performance
    - Customer segments
    - Return impact
    - International markets
    """
)

st.sidebar.divider()

st.sidebar.info(
    "Analysis based on the Online Retail II dataset."
)
st.title("E-Commerce Sales Analytics Dashboard")

st.markdown(
    """
    ### Business Performance Overview

    An interactive analysis of sales, customers, products, markets, and returns.
    """
)

st.info(
    """
    **Key Business Insight:** The United Kingdom is the dominant market, while
    Champions and Loyal / High Potential customers contribute the majority of
    identified-customer revenue. Product-level analysis also highlights
    significant differences between sales volume, revenue contribution, and
    recorded returns.
    """
)
st.divider()

# -----------------------------
# Key Performance Indicators
# -----------------------------

total_revenue = 10272136.23
total_units = 5812948
identified_customers = 4312
return_rate = 3.67
total_orders = 28816

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Total Revenue",
    "£10.27M"
)

col2.metric(
    "Units Sold",
    "5.81M"
)

col3.metric(
    "Orders",
    f"{total_orders:,}"
)

col4.metric(
    "Identified Customers",
    f"{identified_customers:,}"
)

col5.metric(
    "Return Rate",
    f"{return_rate:.2f}%"
)

# -----------------------------
# Sales Performance
# -----------------------------

st.divider()

st.header("📈 Sales Performance")

# Prepare paid sales data
paid_sales = df[df["Quantity"] > 0].copy()

paid_sales["SalesValue"] = (
    paid_sales["Quantity"] * paid_sales["Price"]
)

# -----------------------------
# Monthly Revenue + Top Products
# -----------------------------

col1, col2 = st.columns(2)

with col1:

    st.subheader("Monthly Revenue Trend")

    monthly_revenue = (
        paid_sales
        .set_index("InvoiceDate")
        .resample("ME")["SalesValue"]
        .sum()
    )

    st.line_chart(monthly_revenue)


with col2:

    st.subheader("Top 10 Products by Revenue")

    top_products = (
        paid_sales.groupby("Description")["SalesValue"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .sort_values()
    )

    st.bar_chart(top_products)


# -----------------------------
# Country + Product Analysis
# -----------------------------

col1, col2 = st.columns(2)

with col1:

    st.subheader("Top 10 Countries by Revenue")

    country_revenue = (
        paid_sales.groupby("Country")["SalesValue"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .sort_values()
    )

    st.bar_chart(country_revenue)


with col2:

    st.subheader("Product Volume vs Revenue")

    product_analysis = (
        paid_sales.groupby("Description")
        .agg(
            UnitsSold=("Quantity", "sum"),
            Revenue=("SalesValue", "sum")
        )
        .reset_index()
    )

    st.scatter_chart(
        product_analysis,
        x="UnitsSold",
        y="Revenue"
    )


# -----------------------------
# Customer Intelligence
# -----------------------------

st.divider()

st.header("👥 Customer Intelligence")

st.subheader("Customer Segmentation — RFM Analysis")

rfm_counts = pd.Series({
    "Champions": 920,
    "Loyal / High Potential": 1025,
    "Needs Attention": 1126,
    "At Risk / Low Engagement": 1241
})

rfm_revenue = pd.Series({
    "Champions": 5950360.088,
    "Loyal / High Potential": 1721931.782,
    "Needs Attention": 798905.062,
    "At Risk / Low Engagement": 327036.812
})

col1, col2 = st.columns(2)

with col1:

    st.markdown("**Customer Distribution**")

    st.bar_chart(rfm_counts)


with col2:

    st.markdown("**Revenue Contribution**")

    st.bar_chart(rfm_revenue)


# -----------------------------
# Product & Return Analysis
# -----------------------------

st.divider()

st.header("📦 Product & Return Analysis")

col1, col2 = st.columns(2)

with col1:

    st.subheader("Top Products by Recorded Return Value")

    return_value = (
        df[df["Quantity"] < 0]
        .assign(
            ReturnValue=lambda x: x["Quantity"] * x["Price"]
        )
        .groupby("Description")["ReturnValue"]
        .sum()
        .abs()
        .sort_values(ascending=False)
        .head(10)
        .sort_values()
    )

    st.bar_chart(return_value)


with col2:

    st.subheader("Overall Return Metrics")

    total_return_units = 579417
    cancellation_return_rate = 3.67
    return_value_total = 629808.65

    st.metric(
        "Recorded Return Value",
        f"£{return_value_total:,.2f}"
    )

    st.metric(
        "Returned Units",
        f"{total_return_units:,}"
    )

    st.metric(
        "Cancellation-Based Return Rate",
        f"{cancellation_return_rate:.2f}%"
    )


# -----------------------------
# Operational & Market Insights
# -----------------------------

st.divider()

st.header("⏱️ Operational & Market Insights")

# -----------------------------
# Sales by Hour
# -----------------------------

st.subheader("Sales Revenue by Hour")

hourly_revenue = (
    paid_sales
    .assign(Hour=paid_sales["InvoiceDate"].dt.hour)
    .groupby("Hour")["SalesValue"]
    .sum()
)

st.bar_chart(hourly_revenue)


# -----------------------------
# International Markets
# -----------------------------

st.subheader("International Markets by Average Order Value")

international_sales = paid_sales[
    paid_sales["Country"] != "United Kingdom"
].copy()

international_market = (
    international_sales
    .groupby("Country")
    .agg(
        Revenue=("SalesValue", "sum"),
        Orders=("Invoice", "nunique")
    )
)

international_market["AvgOrderValue"] = (
    international_market["Revenue"]
    / international_market["Orders"]
)

international_aov = (
    international_market[
        international_market["Orders"] >= 10
    ]
    .sort_values("AvgOrderValue", ascending=False)
    .head(10)
    .sort_values("AvgOrderValue")
)

st.bar_chart(
    international_aov["AvgOrderValue"]
)

# -----------------------------
# Data Quality & Methodology
# -----------------------------

st.divider()

st.header("🔎 Data Quality & Methodology")

st.markdown(
    """
    **Analysis methodology**

    - Revenue is calculated as `Quantity × Price`.
    - Sales performance is based on positive-quantity transactions.
    - Negative-quantity transactions are treated as recorded returns or adjustments.
    - Customer segmentation uses the validated RFM analysis from the notebook.
    - International market analysis excludes the United Kingdom to avoid its
      dominance masking smaller markets.
    - Return analysis should be interpreted carefully because the dataset
      contains cancellation, adjustment, damage, and other non-standard
      transaction descriptions.
    """
)

# -----------------------------
# Dashboard Footer
# -----------------------------

st.divider()

st.caption(
    "E-Commerce Sales Analytics | Python • Pandas • Streamlit | "
    "Business analysis of the Online Retail II dataset"
)