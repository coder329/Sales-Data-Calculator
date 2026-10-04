import streamlit as st

st.set_page_config(
    page_title="Sales Data Calculator",
    page_icon="📊"
)

st.title("📊 Sales Data Calculator")
st.write("Analyze sales data using Python.")

sales = [
    1200,
    1500,
    980,
    1750,
    2200,
    1450,
    1900,
    1250,
    1600,
    2500
]

total_sales = sum(sales)
average_sales = total_sales / len(sales)
highest_sale = max(sales)
lowest_sale = min(sales)

st.subheader("Sales Data")
st.write(sales)

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Sales", total_sales)
    st.metric("Highest Sale", highest_sale)

with col2:
    st.metric("Average Sales", round(average_sales, 2))
    st.metric("Lowest Sale", lowest_sale)

st.subheader("📈 Sales Summary")

st.write("Number of Sales:", len(sales))
st.write("Total Sales:", total_sales)
st.write("Average Sales:", round(average_sales, 2))
st.write("Highest Sale:", highest_sale)
st.write("Lowest Sale:", lowest_sale)

st.success("Sales analysis completed successfully! 🚀")