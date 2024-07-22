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

# Separate the header from the data
header = StudentRecord[0]
rows = StudentRecord[1:]

# Print the data in tabular form
print(tabulate(rows,header, tablefmt='grid'))

# Display the names of students whose marks in English are greater than 50
print("Students with marks in English greater than 50:")
for row in rows:
    if row[header.index('English')] > 50:
        print(row[header.index('stdname')])


# display name and age of top 4 scorer in maths
StudentRecord.sort(rows[header.index('Maths')], reverse=True)
print("Top 4 scorers in Maths:")
for row in rows[:4]:
    print(row[header.index('stdname')], row[header.index('Age')])