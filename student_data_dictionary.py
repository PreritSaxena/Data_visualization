from tabulate import tabulate

#dictionary 
StudentRecord = {
    'std101': {
        'stdname': 'Ashish kumar',
        'standard': '10th',
        'Age': 15,
        'Hindi': 67,
        'English': 89,
        'Maths': 87,
        'Science': 89,
        'computer': 90,
        'Total': 422
    },
    'std102': {
        'stdname': 'Abhishek kumar',
        'standard': '10th',
        'Age': 14,
        'Hindi': 85,
        'English': 45,
        'Maths': 48,
        'Science': 90,
        'computer': 45,
        'Total': 313
    },
    'std103': {
        'stdname': 'Aman',
        'standard': '10th',
        'Age': 15,
        'Hindi': 23,
        'English': 56,
        'Maths': 78,
        'Science': 78,
        'computer': 67,
        'Total': 302
    },
    'std104': {
        'stdname': 'Rahul',
        'standard': '10th',
        'Age': 14,
        'Hindi': 45,
        'English': 67,
        'Maths': 45,
        'Science': 45,
        'computer': 56,
        'Total': 258
    },
    'std105': {
        'stdname': 'Ruby',
        'standard': '10th',
        'Age': 13,
        'Hindi': 89,
        'English': 67,
        'Maths': 89,
        'Science': 93,
        'computer': 65,
        'Total': 403
    },
    'std106': {
        'stdname': 'Suman',
        'standard': '10th',
        'Age': 13,
        'Hindi': 90,
        'English': 46,
        'Maths': 67,
        'Science': 67,
        'computer': 67,
        'Total': 337
    },
    'std107': {
        'stdname': 'Saurabh',
        'standard': '10th',
        'Age': 15,
        'Hindi': 45,
        'English': 23,
        'Maths': 34,
        'Science': 45,
        'computer': 34,
        'Total': 181
    },
    'std108': {
        'stdname': 'Sumit',
        'standard': '10th',
        'Age': 14,
        'Hindi': 23,
        'English': 45,
        'Maths': 67,
        'Science': 78,
        'computer': 90,
        'Total': 303
    },
    'std109': {
        'stdname': 'Kamlesh',
        'standard': '10th',
        'Age': 15,
        'Hindi': 45,
        'English': 56,
        'Maths': 78,
        'Science': 99,
        'computer': 67,
        'Total': 345
    },
    'std110': {
        'stdname': 'Rohan',
        'standard': '10th',
        'Age': 15,
        'Hindi': 34,
        'English': 12,
        'Maths': 24,
        'Science': 45,
        'computer': 56,
        'Total': 171
    }
}

# print(StudentRecord)
table = []
for std_id, details in StudentRecord.items():
    row = [std_id, details['stdname'], details['standard'], details['Age'],
           details['Hindi'], details['English'], details['Maths'],
           details['Science'], details['computer'], details['Total']]
    table.append(row)

# Display the table using tabulate
headers = ['stdid', 'stdname', 'standard', 'Age', 'Hindi', 'English', 
           'Maths', 'Science', 'computer', 'Total']
print(tabulate(table, headers, tablefmt='pretty'))

# Display the names of students whose marks in English are greater than 50
print("Students with marks in English greater than 50:")
for std_id, details in StudentRecord.items():
    if details['English'] > 50:
        print(details['stdname'])
