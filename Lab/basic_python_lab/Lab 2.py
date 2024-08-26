# Ques 1. Check leap year

year = int(input("Enter a year: "))
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
    
    
# Ques 2. Find the Largest Among Three Numbers

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print(f"The largest number among the three is: {largest}")


# Ques 3. Check if a Number is Positive, Negative or 0

number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
    
    
# Ques 4. A toy vendor supplies 3 types of toys: Battery Based Toys, Key-based Toys, and Electrical 
# Charging Based Toys. Vendor gives a discount of 10% on orders for battery-based toys if the order is
# for more than Rs. 1000. On orders of more than Rs. 100 for key-based toys, a discount of 5% is given,
# and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500.
# Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical
# charging based toys. WAP to reads the product code and the order amount and prints out the net amount 
# that the customer is required to pay after the discount.

P_Code = int(input("Enter Product Code (1 for Battery Based Toys, 2 for Key-based Toys, 3 for Electrical Charging Based Toys): "))
Amount = float(input("Enter the order amount: Rs. "))
discount = 0
if P_Code == 1:
    if Amount > 1000:
        discount = 0.10
elif P_Code == 2:
    if Amount > 100:
        discount = 0.05
elif P_Code == 3:
    if Amount > 500:
        discount = 0.10
else:
    print("Invalid product code entered.")
    exit(1)
net_amount = Amount - (Amount * discount)
print(f"Net amount to be paid after discount: Rs. {net_amount:.2f}")


# Ques 5. A transport company charges the fare according to following:
# Distance Charges ->     1-50 8 Rs./Km    ,   51-100 10 Rs./Km    ,    > 100 12 Rs/Km

distance = float(input("Enter the distance traveled in kilometers: "))
fare = 0
if distance <= 50:
    fare = distance * 8
elif 51 <= distance <= 100:
    fare = distance * 10
else:
    fare = distance * 12
print(f"The total fare for traveling {distance} km is: Rs. {fare:.2f}")


# Ques 6. WAP to reverse a number using a while loop.

number = int(input("Enter a number: "))
reversed_number = 0
while number > 0:
    remainder = number % 10
    reversed_number = (reversed_number * 10) + remainder
    number = number // 10
print("Reversed number:", reversed_number)


# Ques 7. WAP to check whether a number is palindrome or not

number = int(input("Enter a number: "))
original_number = number
reversed_number = 0
while number > 0:
    remainder = number % 10
    reversed_number = (reversed_number * 10) + remainder
    number = number // 10
if original_number == reversed_number:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")


# Ques 8. WAP finding the factorial of a given number using a while loop.

number = int(input("Enter a number: "))
factorial = 1
i = 1
while i <= number:
    factorial *= i
    i += 1
print(f"Factorial of {number} "is" {factorial}")


# Ques 9. Accept numbers using input() function until the user enters 0. 
# If user input 0 then break the while loop and display the sum of all the numbers.

sum = 0
while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        break
    sum += number
print("The sum of all numbers is:",sum)


# Ques 10. Print the first 10 natural numbers using for loop

for i in range(1, 11):
    print(i)


# Ques 11. Python program to check if the given string is a palindrome

string = input("Enter a string: ")
string = string.lower()
if string == string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


# Ques 12. Python program to check if a given number is an Armstrong number

number = int(input("Enter a number: "))
num_str = str(number)
num_digits = len(num_str)
sum_of_powers = 0
for digit in num_str:
    sum_of_powers += int(digit) ** num_digits
if sum_of_powers == number:
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")
    
    
# Ques 13. Python program to get the Fibonacci series between 0 to 50

a, b = 0, 1
print("Fibonacci series between 0 and 50:")
while a <= 50:
    print(a, end=' ')
    a, b = b, a + b


# Ques 14. Python program to check the validity of password input by users

import re
def is_valid_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True
password = input("Enter your password: ")
if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is invalid.")