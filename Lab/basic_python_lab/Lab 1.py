# Ques1. Take one number from the user and using ternary operators check whether the number is even or odd

number = int(input("Enter a number: "))
result = "Even" if number % 2 == 0 else "Odd"
print(f"The number {number} is {result}")


# Ques2. Take two number and then swap the number

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
print(f"Before swapping: num1 = {num1}, num2 = {num2}")
num1, num2 = num2, num1
print(f"After swapping: num1 = {num1}, num2 = {num2}")


# Ques3. WAP to Convert Kilometers to Miles

factor = 0.621371
kilometers = float(input("Enter distance in kilometers: "))
miles = kilometers * factor
print(f"{kilometers} kilometers is equal to {miles} miles.")


# Ques4. Find the Simple Interest on Rs. 200 for 5 years at 5% per year

Amount = 200
Rate = 5
Time = 5
Simple_Interest = (Amount * Rate * Time) / 100
print(f"The Simple Interest is: Rs. {Simple_Interest}")