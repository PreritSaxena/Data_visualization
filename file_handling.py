# file =  open('example1.txt', 'w')
# file.close()

# with open('example.txt', 'w') as file:
#     file.write('This is new content.')

# # append
# with open('example.txt', 'a') as file:
#     file.write('This will be added to the end.')

# r+
# with open('example.txt', 'r+') as file:
#     content = file.read()
#     print(content)
#     file.write('Adding more content.')

# file = open('example.txt', 'r')
# print(file.tell())
# # content = file.read()
# # print(content)
# file.seek(5)
# data = file.read(10)
# print(data)
# print(file.tell())
# file.close()

# search
# search_keyword = input("Enter the keyword to search: ")
# with open('example.txt' , 'r') as file:
#     for line in file:
#         if search_keyword.lower() in line.lower():
#             print(f"Search completed for keyword: {search_keyword.strip()} ")
#         else:
            # print("No match found.")

# count = 0       
# search_keyword = ("a" , "e", "i" , "o" , "u")
# with open('example.txt' , 'r') as file:
#     for line in file:
#         for word in line.split():
#             if word[0].lower() in search_keyword:
#                 count += 1
#                 print(count) 


# import csv
# f=open('example.csv','w',newline='')
# writer=csv.writer(f)
# data = (['Name','Age','City'])
# writer.writerow(data)
# f.close()

# f=open('example.csv','a',newline='')
# reader=csv.reader(f)
# li=list(reader)
# for row in li:
#     print(row)  
# f.close()

