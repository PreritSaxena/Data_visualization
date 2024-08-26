import pandas as pd
#task 1
df = pd.read_csv('sales_data.csv')

pivot1 = pd.pivot_table(df, values='Sale Amount', index=['Region', 'Manager', 'Salesman'], aggfunc='sum')

print(pivot1)

# task 2

pivot2 = pd.pivot_table(df, values='Units Sold', index='Item', aggfunc='sum')
print(pivot2)

# task 3

pivot3 = pd.pivot_table(df, values='Units Sold', index=['Region', 'Item'], aggfunc='sum')
print(pivot3)

#task 4
pivot4 = pd.pivot_table(df, values='Sale Amount', index='Manager', aggfunc={'Sale Amount': ['count', 'mean']})
print(pivot4)