import logging
import os

# Logging Errors
script_dir = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(script_dir, 'error_log.txt')
logging.basicConfig(
    filename=log_path,
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s:%(message)s'
)

# Input Validation
def validate_input(prompt):
    try:
        return float(input(prompt))
    except ValueError as e:
        print("Invalid input! Please enter a valid number.")
        logging.error(f"ERROR:root:ValueError occurred: {e}")

# Division with Exception Handling
def safe_divide(first_num, second_num):
    try:
        return first_num / second_num
    except ZeroDivisionError as e:
        print("Oops! Division by zero is not allowed.")
        logging.error(f"root:ZeroDivisionError occurred: {e}")
        return None

# Menu of Operations
print("Welcome to the Error-Free Calculator! Choose an operation:", end=" ")
while True:
    operation = input("1. Addition 2. Subtraction 3. Multiplication 4. Divison 5. Exit > ")
    if operation == "5":
        print("Goodbye!")
        break
    elif operation > "5":
        print("Invalid option. Please choose a valid option.")
    else:
        first_num = validate_input("Enter the first number: ")
        second_num = validate_input("Enter the second number: ")
        try:
            if operation == "1":
                result = first_num + second_num
                print(f"The result of {first_num} + {second_num} is {result}.")
            elif operation == "2":
                result = first_num - second_num
                print(f"The result of {first_num} - {second_num} is {result}.")
            elif operation == "3":
                result = first_num * second_num
                print(f"The result of {first_num} * {second_num} is {result}.")
            elif operation == "4":
                result = safe_divide(first_num, second_num)
                if result is not None:
                    print(f"The result of {first_num} / {second_num} is {result}.")
        except TypeError as e:
            print("Type error occurred! Please make sure both inputs are valid numbers.")
            logging.error(f"root:TypeError occurred: {e}")
        except Exception as e:
            print("An unexpected error occurred.")
            logging.error(f"root:An unexpected error occurred: {e}")