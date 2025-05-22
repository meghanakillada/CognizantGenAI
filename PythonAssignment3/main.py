# Task 1 String Slicing and Indexing
string = "Python is amazing"
first_word = string[0:6]
last_word = string[10:17]
reversed_string = string[::-1]
print("First word:", first_word)
print("Amazing part:", last_word)
print("Reversed string:", reversed_string)

# Task 2 String Methods
string = " hello, python world! "
print("Original string:", string)
string = string.strip()
string = string.capitalize()
string = string.replace("world", "universe")
string = string.upper()
print("Modified string:", string)

# Task 3 Check for Palindrome
input_string = input("Enter a word: ")
if input_string == input_string[::-1]:
    print(f"Yes, '{input_string}' is a palindrome!")
else:
    print(f"No, '{input_string}' is not a palindrome!")