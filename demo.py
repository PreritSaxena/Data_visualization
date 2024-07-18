# x=50
# li = []
# while(x<1000):
#     if(x%4 == 0):
#         li.append(x)
#     x+=1

# print(li)



# elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
#             11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


# for i in range(len(elements) - 1, -1, -1):
#     print(elements[i])
    
# elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
#             11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# for i in range(len(elements)):
#     print(elements[-i-1])

# elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
#             11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# for i in reversed(elements):
#     print(i) 

# li = [20,30,40,50]
# x = int(input("Enter a number: "))
# li.append([3,4,5])
# print(li)

# removing element from list 
# firstList = [10,20,30,40,50]
# firstList.pop(2)
# print(firstList)
# print(firstList[1:4])


# deleting element in given range
# del listname[startIndex : endIndex : step]

# firstList = [10,20,30,40,50,60,70,80,90,100]
# firstList.clear()
# # del firstList[1:8:2]
# print(firstList)



# StudentRecord = [
#     ['stdid', 'stdname', 'standard', 'Age', 'Hindi', 'English', 'Maths', 'Science', 'computer', 'Total'],
#     ['std101', 'Ashish kumar', '10th', 15, 67, 89, 87, 89, 90, 422],
#     ['std102', 'Abhishek kumar', '10th', 14, 85, 45, 48, 90, 45, 313],
#     ['std103', 'Aman', '10th', 15, 23, 56, 78, 78, 67, 302],
#     ['std104', 'Rahul', '10th', 14, 45, 67, 45, 45, 56, 258],
#     ['std105', 'Ruby', '10th', 13, 89, 67, 89, 93, 65, 403],
#     ['std106', 'Suman', '10th', 13, 90, 46, 67, 67, 67, 337],
#     ['std107', 'Saurabh', '10th', 15, 45, 23, 34, 45, 34, 181],
#     ['std108', 'Sumit', '10th', 14, 23, 45, 67, 78, 90, 303],
#     ['std109', 'Kamlesh', '10th', 15, 45, 56, 78, 99, 67, 345],
#     ['std110', 'Rohan', '10th', 15, 34, 12, 24, 45, 56, 171]
# ]

# for row in StudentRecord:
#     print(row)

# from tabulate import tabulate

# StudentRecord = [
#     ['stdid', 'stdname', 'standard', 'Age', 'Hindi', 'English', 'Maths', 'Science', 'computer', 'Total'],
#     ['std101', 'Ashish kumar', '10th', 15, 67, 89, 87, 89, 90, 422],
#     ['std102', 'Abhishek kumar', '10th', 14, 85, 45, 48, 90, 45, 313],
#     ['std103', 'Aman', '10th', 15, 23, 56, 78, 78, 67, 302],
#     ['std104', 'Rahul', '10th', 14, 45, 67, 45, 45, 56, 258],
#     ['std105', 'Ruby', '10th', 13, 89, 67, 89, 93, 65, 403],
#     ['std106', 'Suman', '10th', 13, 90, 46, 67, 67, 67, 337],
#     ['std107', 'Saurabh', '10th', 15, 45, 23, 34, 45, 34, 181],
#     ['std108', 'Sumit', '10th', 14, 23, 45, 67, 78, 90, 303],
#     ['std109', 'Kamlesh', '10th', 15, 45, 56, 78, 99, 67, 345],
#     ['std110', 'Rohan', '10th', 15, 34, 12, 24, 45, 56, 171]
# ]

# # Separate the header from the data
# header = StudentRecord[0]
# rows = StudentRecord[1:]

# Print the data in tabular form
# print(tabulate(rows,header, tablefmt='grid'))

#task
# display the name of students whose marks in English is greater than 50

from tabulate import tabulate

StudentRecord = [
    ['stdid', 'stdname', 'standard', 'Age', 'Hindi', 'English', 'Maths', 'Science', 'computer', 'Total'],
    ['std101', 'Ashish kumar', '10th', 15, 67, 89, 87, 89, 90, 422],
    ['std102', 'Abhishek kumar', '10th', 14, 85, 45, 48, 90, 45, 313],
    ['std103', 'Aman', '10th', 15, 23, 56, 78, 78, 67, 302],
    ['std104', 'Rahul', '10th', 14, 45, 67, 45, 45, 56, 258],
    ['std105', 'Ruby', '10th', 13, 89, 67, 89, 93, 65, 403],
    ['std106', 'Suman', '10th', 13, 90, 46, 67, 67, 67, 337],
    ['std107', 'Saurabh', '10th', 15, 45, 23, 34, 45, 34, 181],
    ['std108', 'Sumit', '10th', 14, 23, 45, 67, 78, 90, 303],
    ['std109', 'Kamlesh', '10th', 15, 45, 56, 78, 99, 67, 345],
    ['std110', 'Rohan', '10th', 15, 34, 12, 24, 45, 56, 171]
]


header = StudentRecord[0]
rows = StudentRecord[1:]


print(tabulate(rows, headers=header, tablefmt='grid'))

# Display the names of students whose marks in English are greater than 50
print("Students with marks in English greater than 50:")
for row in rows:
    if row[header.index('English')] > 50:
        print(row[header.index('stdname')])

# display name and age of top 4  scorer in maths
StudentRecord.sort(rows[header.index('Maths')], reverse=True)
print("Top 4 scorers in Maths:")
for row in rows[:4]:
    print(row[header.index('stdname')], row[header.index('Age')])