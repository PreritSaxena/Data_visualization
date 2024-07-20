# x = ["apple" , "banana"]
# y = ["apple" , "banana"]
# z=x

# print(x is z)
# print ("x id is : ", id(x))
# print ("y id is : ", id(y))
# print ("z id is : ", id(z))

# a = "Prerit "
# print(a)
# print(id(a))

# a=a+ "Saxena"
# print(a)
# print(id(a))
# #       0123456789
# name = "i am prerit"
# print(name)
# print("name [2:4]" , name[2:4])
# print("name [5:9]" , name[5:9])
# print("name [:15]" , name[:15])
# print("name [5:]" , name[5:])
# print("name [:]" , name[:])
# print("name [:-1]" , name[:-1])
# print("name [0:15:2]" , name[0:15:2])  
# print("name [::-1]" , name[::-1])

# str = "prerit saxena"
# print(str)
# str.upper()
# print(str)

# str = "Hello"
# str2 = str.center(20)
# print("old" , str)
# print("new :" , str2)


# str = "I am prerit rrrrr"
# oc = str.count("r" , 6)
# print(oc)

# str = "Hello i am in class"
# isends = str.endswith("class")
# print(isends)

# str = "Hello i am in class"
# istarts = str.startswith(" i" , 5, 10)
# print(istarts)

# str = "Hello i am in class"
# find = str.find("am")
# print(find)

# str = "Hello i am in class"
# find = str.index("i")
# print(find)

# str = "abec"
# str2 = str.isalnum()
# print(str2)

# str = "abecD"
# str2 = str.islower()
# print(str2)

# str = "anant"
# str = str.upper()
# print(str)

# str = "*****Prerit     "
# str = str.rstrip()
# print(str)

numeric = 0
alpha = 0
special = 0

str = "123456 preritsaxena  .$*"
for i in str:
    print(i, end=" ") 
    if i.isnumeric():
        numeric += 1 
    elif i.isalpha():
        alpha += 1
    else:
        special += 1
print("Numeric : ", numeric)
print("Alpha : ", alpha)
print("Special : ", special)