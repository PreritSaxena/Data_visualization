import numpy as np

# Ques1. Temperature exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day)

temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2, 4.0, 30.0, 14.0, -4.0, -12.0])

hot_days = np.where(temperatures > 35)[0]
hot_temps = temperatures[hot_days]
print("Hot Days:")
print("Day   Temperature (°C)")
for day, temp in zip(hot_days + 1, hot_temps):  
    print(f"{day:2}    {temp:5.1f}")

cold_days = np.where(temperatures < 5)[0]
cold_temps = temperatures[cold_days]
print("\nCold Days:")
print("Day   Temperature (°C)")
for day, temp in zip(cold_days + 1, cold_temps):  
    print(f"{day:2}    {temp:5.1f}")
    

# Ques2. Split data into quarterly reports for analysis and reporting purposes

monthly_sales = np.array([120, 135, 148, 165, 180, 155, 168, 190, 205, 198, 210, 225])
Q1 = monthly_sales[:3]
Q2 = monthly_sales[3:6]
Q3 = monthly_sales[6:9]
Q4 = monthly_sales[9:12] 
print("Quarter 1 Sales (in thousands of dollars):\n", Q1)
print("Quarter 2 Sales (in thousands of dollars):\n", Q2)
print("Quarter 3 Sales (in thousands of dollars):\n", Q3)
print("Quarter 4 Sales (in thousands of dollars):\n", Q4)


# Ques3. Split data into two groups: one group for customers who made a purchase in the last 30 days and 
# another group for customers who haven't made a purchase in the last 30 days.

import numpy as np

customer_ids = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110])
last_purchase_days_ago = np.array([5, 15, 20, 25, 30, 35, 40, 45, 50, 55])

recent_customers = customer_ids[last_purchase_days_ago <= 30]

non_recent_customers = customer_ids[last_purchase_days_ago > 30]

print("Customers who made a purchase in the last 30 days:\n", recent_customers)
print("Customers who haven't made a purchase in the last 30 days:\n", non_recent_customers)


# Ques4.Suppose two sets of employee data—one containing info about full-time employees and
# another containing info about part-time employee. Combine data to create a comprehensive employee dataset for HR analysis.

full_time_employees = np.array([
    [101, 'John Doe', 'Full-Time', 55000],
    [102, 'Jane Smith', 'Full-Time', 60000],
    [103, 'Mike Johnson', 'Full-Time', 52000]])

part_time_employees = np.array([
    [201, 'Alice Brown', 'Part-Time', 25000],
    [202, 'Bob Wilson', 'Part-Time', 28000],
    [203, 'Emily Davis', 'Part-Time', 22000]])

all_employees = np.concatenate((full_time_employees, part_time_employees), axis=0)

print("Comprehensive employee dataset:")
print(all_employees)


# Ques1. How to find the mean of every NumPy array in the given list?

arrays_list = [
    np.array([3, 2, 8, 9]),
    np.array([4, 12, 34, 25, 78]),
    np.array([23, 12, 67])]

means = [np.mean(arr) for arr in arrays_list]

print("Means of each array:\n", means)


# Ques2. Compute the median of the flattened NumPy array

x_odd = np.array([1, 2, 3, 4, 5, 6, 7])

median_value = np.median(x_odd)

print("Printing Original array:\n",x_odd)
print("Median of the array:\n", median_value)


# Ques3.Compute the standard deviation of the NumPy array

arr = np.array([20, 2, 7, 1, 34])

std_default = np.std(arr)

arr_float32 = arr.astype(np.float32)
std_float32 = np.std(arr_float32)

arr_float64 = arr.astype(np.float64)
std_float64 = np.std(arr_float64)

print(f"arr : {arr.tolist()}")
print(f"std of arr : {std_default}")
print("\nMore precision with float32")
print(f"std of arr : {std_float32:.6f}")
print("\nMore accuracy with float64")
print(f"std of arr : {std_float64}")


# Ques4. Suppose you have a CSV file named 'house_prices.csv' with price information, and perform following operations:
# a.Read the data from the CSV file into a NumPy array.
# b.Calculate the average of house prices.
# c.Identify house price above the average.
# d.Save the list of high prices to a new CSV file.

import pandas as pd

house_data = pd.read_csv('C:\\Users\\SAMYAK\\Desktop\\vs code\\Lab\\Lab 2\\house_prices.csv')

average_price = house_data['House Price'].mean()
print(f"Average House Price: {average_price}")

high_price_houses = house_data[house_data['House Price'] > average_price]

print("High-Pricing Houses:")
print(high_price_houses[['House ID', 'House Price']])

high_price_houses.to_csv('C:\\Users\\Desktop\\vs code\\Lab\\Lab 2\\high_price.csv', index=False)

print("CSV file 'high_price.csv' created with high-pricing houses.")