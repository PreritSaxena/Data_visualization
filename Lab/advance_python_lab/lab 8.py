import pandas as pd
import matplotlib.pyplot as plt


#question - 1
# Input data
student_data = pd.DataFrame({
    'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['V', 'VI', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']
})

# Group by 'class' and count number of students
class_counts = student_data.groupby('class').size()

# Output
print("Number of students in each class:")
print(class_counts)

# Plotting the bar chart
class_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Number of Students in Each Class')
plt.xlabel('Class')
plt.ylabel('Number of Students')
plt.show()

# Conclusion explanation
print("Conclusion: The bar chart shows that Class VI has more students compared to Class V, indicating a higher enrollment in Class VI.")



# question - 2

# Input data
student_data = pd.DataFrame({
    'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']
})

# Group by 'school_code' and calculate mean, min, and max of 'age'
school_stats = student_data.groupby('school_code')['age'].agg(['mean', 'min', 'max'])

# Output
print("Mean, Min, and Max age for each school:")
print(school_stats)

# Plotting the horizontal bar chart
school_stats.plot(kind='barh')
plt.title('Age Statistics by School Code')
plt.xlabel('Age')
plt.ylabel('School Code')
plt.show()

# Conclusion explanation
print("Conclusion: The horizontal bar chart shows age statistics for each school. Schools have varying age distributions, with some schools having a wider range of ages than others.")



# question - 3

# Input data
orders_data = pd.DataFrame({
    'ord_no': [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013],
    'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
    'ord_date': ['2012-10-05', '2012-09-10', '2012-10-05', '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', 
                 '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'],
    'customer_id': [3005, 3001, 3002, 3009, 3005, 3007, 3002, 3004, 3009, 3008, 3003, 3002],
    'salesman_id': [5002, 5005, 5001, 5003, 5002, 5001, 5001, 5006, 5003, 5002, 5007, 5001]
})

# Group by 'customer_id' and calculate mean, min, and max of 'purch_amt'
customer_stats = orders_data.groupby('customer_id')['purch_amt'].agg(['mean', 'min', 'max'])

# Output
print("Mean, Min, and Max purchase amount by customer:")
print(customer_stats)

# Plotting the line chart
customer_stats.plot(kind='line', marker='o')
plt.title('Purchase Amount Statistics by Customer ID')
plt.xlabel('Customer ID')
plt.ylabel('Purchase Amount')
plt.grid(True)
plt.show()

# Conclusion explanation
print("Conclusion: The line chart shows the variability of purchase amounts among customers. Some customers have higher purchase amounts on average, indicating potentially larger or more frequent transactions.")





# question - 4
# Input data
df = pd.DataFrame({
    'ord_no': [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013],
    'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
    'ord_date': ['05-10-2012', '09-10-2012', '05-10-2012', '08-17-2012', '10-09-2012', '07-27-2012', 
                 '10-09-2012', '10-10-2012', '10-10-2012', '06-17-2012', '07-08-2012', '04-25-2012'],
    'customer_id': [3001, 3001, 3005, 3001, 3005, 3001, 3005, 3001, 3005, 3001, 3005, 3005],
    'salesman_id': [5002, 5005, 5001, 5003, 5002, 5001, 5001, 5006, 5003, 5002, 5007, 5001]
})

# Convert 'ord_date' to datetime format and extract month
df['ord_date'] = pd.to_datetime(df['ord_date'], format='%m-%d-%Y')
df['month'] = df['ord_date'].dt.strftime('%Y-%m')

# Group by 'month' and calculate sum of 'purch_amt'
monthly_sales = df.groupby('month')['purch_amt'].sum()

# Output
print("Monthly purchase amount:")
print(monthly_sales)

# Plotting the bar chart
monthly_sales.plot(kind='bar', color='lightgreen', edgecolor='black')
plt.title('Monthly Purchase Amount')
plt.xlabel('Month')
plt.ylabel('Total Purchase Amount')
plt.xticks(rotation=45)
plt.show()

# Conclusion explanation
print("Conclusion: The bar chart shows the monthly purchase amounts, highlighting peak months for sales. This information can be useful for understanding sales trends and planning future strategies.")
