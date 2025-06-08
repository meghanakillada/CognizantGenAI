# Task 1 Understanding Python Exceptions
while True:
    try:
        num = float(input("Enter a number: "))
        result = 100 / num
    except ZeroDivisionError:
        print("Oops! You cannot divide by zero.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    else:
        print(f"100 divided by {num} is {result}.")
        break

# Task 2 Types of Exceptions
list_of_numbers = [1, 2, 3, 4, 5]
dict_of_numbers = {'one': 1, 'two': 2, 'three': 3}
string_value = "Hello"
integer_value = 10
try:
    print(list_of_numbers[5])
except IndexError as e:
    print(f"IndexError occurred! {e}")
try:
    print(dict_of_numbers['four'])
except KeyError as e:
    print(f"KeyError occurred! {e}")
try:
    print(string_value + integer_value)
except TypeError as e:
    print(f"TypeError occurred! {e}")

# Task 3 Using try...except...else...finally
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the first number: "))
try:
    result = first_num / second_num # try block to attempt the division
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.") # except block to handle exceptions
else:
    print(f"The result of {first_num} divided by {second_num} is {result}.") # else block to display the result if no exceptions occur.
finally:
    print("This block always executes.") # finally block to print a closing message regardless of exceptions