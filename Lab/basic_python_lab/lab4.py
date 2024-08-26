# 1 Write a Python program to sum all the items in a list.
 
def sum_list(items):
    return sum(items)

numbers = [1, 2, 3, 4, 5]
total = sum_list(numbers)
print(f"The sum of the list is: {total}")\

# 2 . Write a Python program to get the largest and smallest number from a list without builtin functions.
 
numbers = [34, 15, 88, 2, 90, 3, -2, 43]

largest = smallest = numbers[0]

for num in numbers[1:]:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print(f"The largest number in the list is: {largest}")
print(f"The smallest number in the list is: {smallest}")

# 3  Write a Python program to find duplicate values from a list and display those.
numbers = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 8, 9, 10, 1]

duplicates = []
unique_items = set()

for num in numbers:
    if num in unique_items:
        if num not in duplicates:
            duplicates.append(num)
    else:
        unique_items.add(num)

print("Duplicate values in the list are:", duplicates)


# 4 
original_list = [1, 1, 2, 3, 4, 4, 5, 1]
length_of_first_part = 3
first_part = original_list[:length_of_first_part]
second_part = original_list[length_of_first_part:]
print("Splitted the said list into two parts:")
print((first_part, second_part))

# 5 
colors = ['red', 'green', 'white', 'black']
for i in range(len(colors) - 1, -1, -1):
    print(colors[i])

# Assignment 2

# 1
test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}

total = sum(test_dict.values())
count = len(test_dict)

mean = total / count

print(f"The mean is: {mean}")

# 2
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
concatenated_dict = {}
concatenated_dict.update(dic1)
concatenated_dict.update(dic2)
concatenated_dict.update(dic3)
print(concatenated_dict)

# 3
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("Key\tValue")
for key, value in dict_num.items():
    print(f"{key}\t{value}")


# 4
input_dict = {1: 10, 2: 20, 3: None, 4: 40, 5: None, 6: 60}
filtered_dict = {k: v for k, v in input_dict.items() if v is not None}
print("dict with empty items Dropped :")
print(filtered_dict)

# Assignment 3
# 1
tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7)
count_of_fours = tuplex.count(4)
print(count_of_fours)


# 2
listx = [5, 10, 7, 4, 15, 3]
tuplex = tuple(listx)
print(tuplex)


# 3
tuples_list = [(1, 2), (3, 4), (5, 6)]
total_sum = sum(sum(t) for t in tuples_list)
print("sum of tuple is :", total_sum)

# 4
employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)

employees = [employee1, employee2, employee3]

print("Employee Records :\n")

for emp in employees:
    print(f"Name : {emp[0]}")
    print(f"Employee ID : {emp[1]}")
    print(f"Department : {emp[2]}")
    print(f"Salary : {emp[3]}")
    print()


# Assignment 4
# 1
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
unique_items = set1.union(set2)
print(unique_items)


# 2
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
symmetric_difference = set1.symmetric_difference(set2)
print(symmetric_difference)

# 3
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
symmetric_difference = set1.symmetric_difference(set2)
print(symmetric_difference)

# 4
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.intersection_update(set2)
print(set1)


