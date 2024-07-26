import numpy as np


# 1
# my_list = [1, 2, 3, 4, 5]
# my_array = np.array(my_list)
# print(my_array)

# 2
# convert the below list into array then display the array then display the first and last index then multiply each element by two and display resultt 

# my_list = [1,2,3,4,5]
# my_arr = np.array(my_list)
# print(my_arr)
# print("first element:" ,my_arr[0])
# print("last element :" ,my_arr[-1])
# doubled_array = my_arr * 2
# print("Array with each element multiplied by two:", doubled_array)

# 3
# write a numpy program to create an array of 10 zero , 10 ones and 10 fives
# import numpy as np


# zeros_array = np.zeros(10)
# ones_array = np.ones(10)
# fives_array = np.full(10, 5)

# print("Array of 10 zeros:")
# print(zeros_array)
# print("\nArray of 10 ones:")
# print(ones_array)
# print("\nArray of 10 fives:")
# print(fives_array)


# 4
#write a numpy program to create  3*3 matrix with values ranging form 2 to 10
values = np.arange(2, 11)
matrix = values.reshape((3, 3))
print("3x3 matrix with values ranging from 2 to 10:")
print(matrix)


