import numpy as np

# a = np.array(45)
# b = np.array([1,2,3,4,5])
# c = np.array([[1,2,3],[4,5,6]])
# d = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

# print(a.shape)
# print(b.shape)
# print(c.shape)
# print(d.shape)

# print(a)
# print(b)
# print(c)
# print(d)

# arr = np.array([True,False,True],dtype = np.bool_)
# print(arr)

# arr = np.array(['apple',2,3.7],dtype=np.object_)
# print(arr)

# arr = np.array(['apple','world'],dtype=np.string_)
# print(arr)

# Create a 5x3 array of zeros
# arr = np.zeros((5, 3))
# print("Original array:")
# print(arr)

# np.random.seed(10)
# arr = np.random.randint(1,100,8).reshape(2,4)
# print(arr)

# ar = np.array([1,2,3,4,5,6,7,8,9,10])
# slicing = ar[4:9]
# print(slicing)
# slicing[:] = 0  
# print(slicing)

# ar = np.arange(1,15)
# print(ar)
# print(ar[ar % 2 == 0])
# print(ar[ar % 2 != 0])
# print(ar[ar>8])
# ar[ar % 2 == 0] = 0
# print(ar)

# arr = np.arange(1,8)
# print(arr+2)
# print(arr*2)
# print(arr**2) 

# np.random.seed(10)
# mat= np.random.randint(1,100,5)
# print(mat)
# np.random.shuffle(mat)
# print(mat)
# print(np.unique(mat,return_index=False,return_counts=True))
# print(np.unique(mat).size)

# arr1 = np.array([1,2,3,4,5])
# arr2 = np.array([6,7,8,9,10])
# print(np.vstack((arr1,arr2)))
# # print(np.hstack((arr1,arr2)))

# def custom_cumsum(arr):
#     cumsum = []
#     total = 0
#     for num in arr:
#         total += num
#         cumsum.append(total)
#     return cumsum

# # Example usage
# mat = np.random.randint(1,100,9).reshape(3,3)
# arr = [1, 2, 3, 4]
# print(mat)
# print(custom_cumsum(mat)) 


