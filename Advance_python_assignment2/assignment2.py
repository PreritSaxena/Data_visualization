# lab assignment 

# 1. Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.

with open('ABC.txt', 'r') as file:
    for line in file:
        print(line, end='') 

#2 Write a function in Python to count and display the total number of words in a text file "ABC.txt"
def count_words_in_file(filename="ABC.txt"):
    total_words = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                words = line.split()
                total_words += len(words)
        print(f"Total number of words: {total_words}")
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")


count_words_in_file()

# 3. Write a function in Python to count uppercase character in a text file "ABC.txt"

def count_uppercase_characters(filename="ABC.txt"):
    uppercase_count = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                for char in line:
                    if char.isupper():
                        uppercase_count += 1
        print(f"Total number of uppercase characters: {uppercase_count}")
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")


count_uppercase_characters()

# 4
def display_words(filename="ABC.txt"):
    try:
        with open(filename, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    if len(word) < 4:
                        print(word)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")


display_words()

# 5
# occurence of word INDIA IN FILE anudip.txt

