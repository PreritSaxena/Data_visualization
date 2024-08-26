# 1. Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.

with open("ABC.txt", 'r') as file:
    for line in file:
        print(line, end='')

# 2
with open("ABC.txt", 'r') as file:
    content = file.read()
    words = content.split()
    print(f"Total number of words: {len(words)}")

# 3
with open("ABC.txt", 'r') as file:
    content = file.read()
    uppercase_count = sum(1 for char in content if char.isupper())
    print(f"Total number of uppercase characters: {uppercase_count}")

# 4
with open("story.txt", 'r') as file:
    for line in file:
        words = line.split()
        short_words = [word for word in words if len(word) < 4]
        for word in short_words:
            print(word)

# Assignment 2 
# 1
try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    result = numerator / denominator
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")


# 2
try:
    user_input = input("Enter an integer: ")
    number = int(user_input)
    print(f"You entered: {number}")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")


# 3
filename = "example.txt"

try:
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"Error: The file {filename} does not exist.")


# 4
try:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    result = float(num1) + float(num2)
    print(f"Result: {result}")
except ValueError:
    print("Error: Invalid input. Please enter numerical values.")
