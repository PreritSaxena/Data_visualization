import pandas as pd
import numpy as np

# data = [10,20,30,40,50]
# series = pd.Series(data)
# print(series)
# print(type(series))
# print(data)
# print(type(data))

# D = {40:”john”, 45:”peter”}

# data = {'Name':['John','Peter','Mathew','Tom','Jerry'],
#         'Age':[40,45,50,55,60]}

# df = pd.DataFrame(data)
# print(df)
# print("Inserting gender at 1 index")
# df.insert(1, "Gender" , ["Female" , "Male" , "Female" , "Male" , "Female"])
# print( df)

# CSV file
# data = {
#     'Name': ['John', 'Peter', 'Mathew', 'Tom', 'Jerry'],
#     'Age': [40, 45, 50, 55, 60]
# }
# df = pd.DataFrame(data)
# csv_file_path =  'output.csv'
# df.to_csv(csv_file_path , index = False , columns = ['Name']  , header = ["Student Name"])
# print(f'Data saved to csv file to {csv_file_path}')

# # Excel file
# excel_file_path = 'output.xlsx'
# df.to_excel(excel_file_path , index = False , columns = ['Name']  , header = ["Student Name"])
# print(f'Data saved to excel file to {excel_file_path}')

# df = pd.read_csv("output.csv")
# df.drop_duplicates(subset = "Slot Id" , inplace = True)

data = {
    'Date' : ['2024-01-01' , '2024-01-02' , '2024-01-03' , '2024-01-04' , '2024-01-05'],
    'Category' : ['A' , 'B' , 'C' , 'D' , 'E'],
    'Sales' : [100,200,300,400,500],
    "Quantity" : [10,20,30,40,50]
}

df = pd.DataFrame(data)
pivot_table = pd.pivot_table(
    df,
    index = 'Date',
    values = ['Sales'],
    columns = ['Category'],
    aggfunc = ['sum',"Sum"],
    fill_value = 0
    dropna = False,
    margins=True,
    margins_name='Total'

)

np.round(pivot_table,2)