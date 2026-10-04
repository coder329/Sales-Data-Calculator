# 📊 Interactive Sales Data Calculator

## Task 4 - Level 1 - Day 4

An interactive Python and Streamlit application that allows users to enter **their own sales data** and instantly calculate important sales statistics.

Instead of analyzing only a fixed dataset, this version turns the basic Python task into a **publicly accessible web application** that anyone can use through the live Streamlit link.

---

## 🌐 Live Application

🚀 **Try the Sales Data Calculator:**

https://sales-data-calculator-keuwqch38ask7apl22mkcq.streamlit.app/

Open the application, enter your own sales values, and click **Calculate Sales** to get the results instantly.

---

## 🔗 GitHub Repository

**Source Code and Project Files:**

https://github.com/coder329/Sales-Data-Calculator

---

## 📌 Project Overview

The Sales Data Calculator was created as a beginner-level Python data-analysis project and then extended into an interactive Streamlit web application.

The application accepts sales values entered by the user and calculates:

- Number of sales
- Total sales
- Average sale
- Highest sale
- Lowest sale

The application also performs basic input validation and displays helpful messages when invalid values are entered.

---

## 🎯 Objectives

- Understand basic numerical data analysis using Python
- Work with Python lists and numerical values
- Calculate total, average, highest, and lowest sales
- Accept user-provided sales data
- Validate user input
- Build an interactive web application using Streamlit
- Deploy the application so other users can access it online

---

## 🛠️ Tools & Technologies

- **Python**
- **Jupyter Notebook**
- **VS Code**
- **Streamlit**
- **Git**
- **GitHub**

---

## ⚙️ How the Application Works

### Step 1 — Enter Sales Data

The user enters sales values separated by commas or new lines.

Example:

```text
5000, 7500, 6200, 8100, 4500
```

### Step 2 — Calculate Sales

The user clicks the **Calculate Sales** button.

### Step 3 — Get Instant Results

The application calculates and displays:

```text
Number of Sales
Total Sales
Average Sale
Highest Sale
Lowest Sale
```

---

## 📊 Example

For the following input:

```text
5000, 7500, 6200, 8100, 4500
```

The application calculates:

| Statistic | Result |
|---|---:|
| Number of Sales | 5 |
| Total Sales | 31,300 |
| Average Sale | 6,260 |
| Highest Sale | 8,100 |
| Lowest Sale | 4,500 |

Users can enter any valid sales values and receive new results.

---

## ✅ Input Validation

The application checks the entered data before performing calculations.

It handles:

- Empty input
- Invalid/non-numeric values
- Negative sales values

This helps prevent calculation errors and provides a better user experience.

---

## 🧮 Python Functions Used

The project uses basic Python functions for numerical analysis:

- `sum()` — calculates total sales
- `max()` — finds the highest sale
- `min()` — finds the lowest sale
- `len()` — counts the number of sales

Average sales are calculated using:

```python
average_sales = total_sales / len(sales)
```

---

## 📁 Project Structure

```text
Sales-Data-Calculator/
│
├── Sales_Data_Calculator.ipynb
├── Sales_Data_Calculator.py
├── Streamlit_app.py
└── readme.md
```

---

## 📓 Jupyter Notebook

`Sales_Data_Calculator.ipynb` contains the step-by-step implementation of the Task 4 sales analysis using Python.

It demonstrates:

- Creating sales data
- Calculating total sales
- Calculating average sales
- Finding highest and lowest sales
- Verifying the calculations
- Basic interview questions and learning outcomes

---

## 🐍 Python Program

`Sales_Data_Calculator.py` contains the basic Python implementation of the sales analysis task.

It demonstrates the core numerical calculations required by the assignment.

---

## 🌐 Streamlit Application

`Streamlit_app.py` converts the basic Python analysis into an interactive application.

Unlike the original fixed-data version, users can enter their **own sales values** and receive the calculated output dynamically.

---

## ▶️ Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/coder329/Sales-Data-Calculator.git
```

### 2. Open the project folder

```bash
cd Sales-Data-Calculator
```

### 3. Install Streamlit

```bash
pip install streamlit
```

### 4. Run the Streamlit application

```bash
streamlit run Streamlit_app.py
```

The application will open in your web browser at a local Streamlit address.

---

## 💡 What I Learned

Through this project, I practiced:

- Python lists
- Numerical calculations
- `sum()`, `max()`, `min()`, and `len()`
- Average calculation
- User input handling
- Data validation
- Exception handling
- Streamlit application development
- Deploying a Python application online
- Git and GitHub
- Project documentation

---

## 🚀 Future Improvements

Possible future improvements include:

- Sales charts and visualizations
- CSV file upload
- Monthly and yearly sales analysis
- Product-wise sales analysis
- Downloadable analysis reports
- Interactive filters
- Sales trend visualization

---

## 👨‍💻 Author

**Saksham**

AI & ML Learner | Python | Data Analysis | Streamlit | GitHub

---

## 🔗 Project Links

🌐 **Live Streamlit App:**  
https://sales-data-calculator-keuwqch38ask7apl22mkcq.streamlit.app/

🔗 **GitHub Repository:**  
https://github.com/coder329/Sales-Data-Calculator
