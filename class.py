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

# numeric = 0
# alpha = 0
# special = 0

# str = "123456 preritsaxena  .$*"
# for i in str:
#     print(i, end=" ") 
#     if i.isnumeric():
#         numeric += 1 
#     elif i.isalpha():
#         alpha += 1
#     else:
#         special += 1
# print("Numeric : ", numeric)
# print("Alpha : ", alpha)
# print("Special : ", special)

# 22-7-24
# oops
# class student:
#     name = 'abcd'
#     age = 0
#     def study(self):
#         print("I am studying")

# student().study(1)
# obj = student()
# obj.study()

# use of self in class
# def show() :
#     print("outside")

# class student:
#     def study(self):
#         self.show()
#         print("I am studying")  

#     def show(self):
#         print("inside")

# obj = student()
# obj.study()

# Inheritance
# class A:
#     name:"prerit"
#     def show(self):
#         print("I am in class A")

# class B(A):
#     def showb(self):
#         print("I am in class B")
#     pass

# obj = B()
# obj.show()

# multilevel inheritance
# class C(B):
#     def showc(self):
#         print("I am in class C")

# class D(C,B):
#     pass

# obj = D()
# obj.show()
# obj.showb()
# obj.showc()


# function over riding
# def setData(name , age):
#     print("Name : ", name)
#     print("Age : ", age)

# def setData(name , age , city):
#     print("Name : ", name)
#     print("Age : ", age)
#     print("City : ", city)


# setData("Prerit" , 20 , "Delhi")

# method over riding
# Polymorphism lets us define methods in the child class that have the same name as the methods in the parent class, In inheritance, the child class inherits the methods from the parent class. However, it is possible to modify a method in a child class that it has inherited from the parent class. This is particularly useful in cases where the method inherited from the parent class doesn't quite fit the child class. In such cases, we re-implement the method in the child class. This process of re-implementing a method in the child class is known as Method Overriding.

# example of method over riding

# class Bird:
#     def intro(self):
#         print("There are many types of birds.")

#     def flight(self):
#         print("Most of the birds can fly but some cannot.")

# class sparrow(Bird):
#     def flight(self):
#         print("Sparrows can fly.")

# class ostrich(Bird):
#     def flight(self):
#         print("Ostriches cannot fly.")

# obj_bird = Bird()
# obj_spr = sparrow()
# obj_ost = ostrich()

# # obj_bird.intro()
# # obj_bird.flight()
# obj_spr.flight()

# exception handling
#       1 print('line 1')
# print('line 2')
# print('line 3')
# print('line 4')
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("You cannot divide by zero")
# print('line 5')
# print('line 6')
# print('line 7')

# try with multiple expect
print('line 1')
print('line 2')
print('line 3')
print('line 4')
try:
    print(10/0)

except ZeroDivisionError:
    print("You cannot divide by zero")
try:
  open("abc.txt")
except FileNotFoundError:
    print("File not found")
print('line 5')
print('line 6')
print('line 7')