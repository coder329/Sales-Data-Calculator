# Sales Data Calculator
# Task 4 - Level 1 - Day 4

# Store sales values in a Python list
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

# Calculate sales statistics
total_sales = sum(sales)
average_sales = total_sales / len(sales)
highest_sale = max(sales)
lowest_sale = min(sales)

# Display results
print("===== Sales Data Calculator =====")
print("Sales Values:", sales)
print("Number of Sales:", len(sales))
print("Total Sales:", total_sales)
print("Average Sales:", round(average_sales, 2))
print("Highest Sale:", highest_sale)
print("Lowest Sale:", lowest_sale)