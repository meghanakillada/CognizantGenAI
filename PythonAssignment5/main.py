# Task 1 Writing Functions
def greet_user(name):
    print(f"Hello, {name}! Welcome aboard.", end=" ")
def add_numbers(num1, num2):
    return num1 + num2
greet_user("Alice")
result = add_numbers(5, 10)
print(f"The sum of 5 and 10 is {result}.")

# Task 2 Using Default Parameters
def describe_pet(pet_name, pet_type="dog"):
    print(f"I have a {pet_type} named {pet_name}.", end=" ")
describe_pet("Buddy")
describe_pet("Whiskers", "cat")

# Task 3 Functions with Variable Arguments
def make_sandwich(*ingredients):
    print("Making a sandwich with the following ingredients:", end=" ")
    for ingredient in ingredients:
        print(f"- {ingredient}", end=" ")
print()
make_sandwich("Lettuce", "Tomato", "Cheese")

# Task 4 Understanding Recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print()
print(f"Factorial of 5 is {factorial(5)}.", end=" ")

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(f"The 6th Fibonacci number is {fibonacci(6)}.")