# Task 1 Counting Down with Loops
starting_number = int(input("Enter the starting number: "))
while starting_number > 1:
    print(starting_number, end=" ")
    starting_number -= 1
print("Blast off!🚀")

# Task 2 Multiplication with for Loops
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}", end=" ")

# Task 3 Find the Factorial
number = int(input("\nEnter a number: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"The factorial of {number} is {factorial}.")