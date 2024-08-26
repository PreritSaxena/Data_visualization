# Ques 1. Declare a div() function with two parameters. 
# Then call the function and pass two numbers and display their division.

def div(a, b):
    if b == 0:
        return "Division by zero is not allowed."
    else:
        return a / b
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = div(num1, num2)
print("The result of the division is:", result)


# Ques 2. Declare a square() function with one parameter.
# Then call the function and pass one number and display the square of that number .

def square(x):
    return x * x
num = float(input("Enter a number: "))
result = square(num)
print("The square of", num, "is:", result)


# Ques 3. Using max() and min() functions display the maximum and minimum of 5 random numbers.

import random
numbers = [random.randint(1, 100) for _ in range(5)]
print("The numbers are:", numbers)
max_num = max(numbers)
min_num = min(numbers)
print("The maximum number is:", max_num)
print("The minimum number is:", min_num)


# Ques 4. Accept a name from the user and display that in lower case using lower() function

name = input("Enter your name: ")
lowercase_name = name.lower()
print("Your name in lowercase is:", lowercase_name)


# Ques 1. Write a Python program to count the occurrences of each word in a given sentence

sentence = "To change the overall look of your document. To change the look available in the gallery"
sentence = sentence.replace('.', '').replace(',', '')
words = sentence.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print("Word occurrences:")
for word, count in word_count.items():
    print(f"'{word}': {count}")


# Ques 2. Write a Python program to remove a newline in Python

string = "\nBest \nDeeptech \nPython \nTraining\n"
cleaned_string = string.replace('\n', '')
print("Cleaned string:", cleaned_string)


# Ques 3. Write a Python program to reverse words in a string

string = "Deeptech Python Training"
words = string.split()
reversed_words = words[::-1]
reversed_string = ' '.join(reversed_words)
print("Reversed words string:", reversed_string)


# Ques 4. Write a Python program to count and display the vowels of a given text

string = "Welcome to python Training"
vowels = 'aeiouAEIOU'
vowel_count = {vowel: 0 for vowel in vowels}
for char in string:
    if char in vowel_count:
        vowel_count[char] += 1
print("Vowel counts:")
for vowel, count in vowel_count.items():
    if count > 0:
        print(f"'{vowel}': {count}")


# Ques 1.  WAP to Count all letters, digits, and special symbols from the given string

input_string = "P@#yn26at^&i5ve"
char_count = 0
digit_count = 0
symbol_count = 0
for char in input_string:
    if char.isalpha():
        char_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        symbol_count += 1
print(f"Chars = {char_count}")
print(f"Digits = {digit_count}")
print(f"Symbols = {symbol_count}")


# Ques 2. Write a Python program to remove duplicate characters of a given string.

input_string = "String and String Function"
seen = set()
result = []
for char in input_string:
    if char not in seen:
        seen.add(char)
        result.append(char)
output_string = ''.join(result)
print("Output:", output_string)


# Ques 3. WAP to count Uppercase, Lowercase, special character and numeric values in a given string

input_string = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
uppercase_count = 0
lowercase_count = 0
numeric_count = 0
special_count = 0
for char in input_string:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
    elif char.isdigit():
        numeric_count += 1
    elif not char.isspace():
        special_count += 1
print(f"UpperCase : {uppercase_count}")
print(f"LowerCase : {lowercase_count}")
print(f"NumberCase : {numeric_count}")
print(f"SpecialCase : {special_count}")


# Ques 4.  Write a Python Count vowels in a string

input_string = "Welcome to Python Assignment"
vowels = 'aeiouAEIOU'
vowel_count = 0
for char in input_string:
    if char in vowels:
        vowel_count += 1
print(f"Total vowels are: {vowel_count}")