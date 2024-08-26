import pandas as pd


#question - 1
# Input data
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack']
exam_scores = [92, 88, 76, 94, 82, 90, 85, 89, 78, 91]

# Create Pandas Series
scores_series = pd.Series(exam_scores, index=students)

# Output
print("Exam Scores of Students:")
print(scores_series)


#question - 2
# Input data
categories = ['Groceries', 'Utilities', 'Rent', 'Transportation', 'Entertainment']
expenses = [500, 200, 1200, 300, 150]

# Create Pandas Series
expenses_series = pd.Series(expenses, index=categories)

# Output
print("Household Expenses for a Month:")
print(expenses_series)


#question - 3

# Input data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
electricity_usage = [350, 320, 310, 330, 340, 370, 380, 360, 350, 330, 320, 330]
gas_usage = [20, 18, 16, 15, 12, 10, 8, 9, 12, 15, 17, 19]

# Create Pandas Series for electricity and gas usage
electricity_series = pd.Series(electricity_usage, index=months)
gas_series = pd.Series(gas_usage, index=months)

# Output
print("Monthly Electricity Usage (kWh):")
print(electricity_series)
print("\nMonthly Gas Usage (therms):")
print(gas_series)


#question - 4

# Input data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
revenue = [5000, 5200, 4800, 5400, 5600, 5800, 6100, 5900, 6200, 6500, 7000, 6900]

# Create Pandas Series
revenue_series = pd.Series(revenue, index=months)

# Output
print("Monthly Advertising Revenue (USD):")
print(revenue_series)
