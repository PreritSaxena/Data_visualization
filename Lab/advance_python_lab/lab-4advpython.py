#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
x = [0, 5, 9, 10, 15, 20, 25]
y = [0, 1, 2, 3, 4, 5, 6]
plt.plot(x, y)
plt.show()


# In[2]:


# question=1-----------------------------------

# Lab1: Visualize the daily temperature changes over time in a city and give your
# conclusion
# Input:

# days = list(range(1, 32))
# # Daily temperature data (replace with your own data)
# temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78,
# 80, 81, 82, 83, 82, 80, 78, 76, 74, 71]




days = list(range(1, 32))
# Daily temperature data (replace with your own data)
temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78,
               80, 81, 82, 83, 82, 80, 78, 76, 74, 71]
plt.plot(days, temperature, marker='.')
plt.xlabel("day of the month")
plt.ylabel("temprature (*f)")
plt.title("daily temperature over a month ")
plt.show()


# In[3]:


# queston 1---------------------------------



# Lab2: Create a line plot to visualize the daily closing prices of a stock over a year
# and give your conclusion.
# Input:
# days = list(range(1, 78))
# # Daily closing prices of a stock (replace with your own data)
# stock_prices = [100, 105, 110, 115, 112, 120,
# 118, 125, 128, 130, 132, 135,
# 138, 140, 142, 144, 145, 148,
# 150, 155, 160, 158, 162, 165,
# 170, 172, 175, 178, 180, 182,
# 185, 188, 190, 192, 195, 198,
# 200, 198, 195, 193, 190, 188,
# 185, 182, 180, 178, 175, 172,
# 170, 168, 165, 162, 160, 158,
# 155, 152, 150, 148, 145, 143,
# 140, 138, 135, 132, 130, 128,
# 125, 123, 120, 118, 115, 112,
# 110, 108, 105, 103, 100]



import matplotlib.pyplot as plt

# Days and stock prices
days = list(range(1, 78))
stock_prices = [
    100, 105, 110, 115, 112, 120, 118, 125, 128, 130, 132, 135,
    138, 140, 142, 144, 145, 148, 150, 155, 160, 158, 162, 165,
    170, 172, 175, 178, 180, 182, 185, 188, 190, 192, 195, 198,
    200, 198, 195, 193, 190, 188, 185, 182, 180, 178, 175, 172,
    170, 168, 165, 162, 160, 158, 155, 152, 150, 148, 145, 143,
    140, 138, 135, 132, 130, 128, 125, 123, 120, 118, 115, 112,
    110, 108, 105, 103, 100
]

plt.figure(figsize=(12, 6))
plt.plot(days, stock_prices, marker='o', linestyle='-', color='b')

plt.title('Stock Prices Over Time')
plt.xlabel('Days')
plt.ylabel('Stock Prices')

plt.grid(True)
plt.show()







