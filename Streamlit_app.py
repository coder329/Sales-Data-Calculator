import streamlit as st

st.set_page_config(
    page_title="Sales Data Calculator",
    page_icon="📊",
    layout="centered"
)

# Title
st.title("📊 Sales Data Calculator")
st.write(
    "Enter your sales values below and calculate total, average, "
    "highest, and lowest sales."
)

st.divider()

# User input
st.subheader("📝 Enter Your Sales Data")

sales_input = st.text_area(
    "Enter sales values separated by commas or new lines:",
    placeholder="Example: 1200, 1500, 980, 1750, 2200",
    height=150
)

# Calculate button
if st.button("Calculate Sales", type="primary"):

    if not sales_input.strip():
        st.warning("Please enter at least one sales value.")

    else:
        try:
            # Replace new lines with commas
            cleaned_input = sales_input.replace("\n", ",")

            # Convert input values into numbers
            sales = [
                float(value.strip())
                for value in cleaned_input.split(",")
                if value.strip()
            ]

            if not sales:
                st.warning("Please enter valid sales values.")

            elif any(value < 0 for value in sales):
                st.error("Sales values cannot be negative.")

            else:
                # Calculations
                total_sales = sum(sales)
                average_sales = total_sales / len(sales)
                highest_sale = max(sales)
                lowest_sale = min(sales)

                st.success("Sales analysis completed successfully! ✅")

                st.divider()

                # Metrics
                st.subheader("📈 Sales Results")

                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                        "Number of Sales",
                        len(sales)
                    )

                    st.metric(
                        "Total Sales",
                        f"{total_sales:,.2f}"
                    )

                with col2:
                    st.metric(
                        "Average Sale",
                        f"{average_sales:,.2f}"
                    )

                    st.metric(
                        "Highest Sale",
                        f"{highest_sale:,.2f}"
                    )

                st.metric(
                    "Lowest Sale",
                    f"{lowest_sale:,.2f}"
                )

                st.divider()

                # Show entered data
                st.subheader("📋 Your Sales Data")

                formatted_sales = [
                    f"{value:,.2f}" for value in sales
                ]

                st.write(formatted_sales)

        except ValueError:
            st.error(
                "Invalid input. Please enter only numbers separated "
                "by commas or new lines."
            )

st.divider()

st.caption(
    "Sales Data Calculator | Built with Python and Streamlit"
)