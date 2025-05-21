# Task 1 Variables
name = "Maggie"
age = 20
height = 5.4
print("Hey there, my name is " + name + "! I am " + str(age) + " years old and " + str(height) + " feet tall.")

# Task 2 Operators: Playing with Numbers
num1 = 20
num2 = 5
print("The sum of 20 and 5 is", num1 + num2) #addition
print("The difference between 20 and 5 is", num1 - num2) #subtraction
print("The product of 20 and 5 is", num1 * num2) #multiplication
print("The result of dividing 20 by 5 is", num1 / num2) #division

# Task 3 Conditional Statements: The Number Checker
number = int(input("Enter a number, any number (positive, negative, or zero): "))
if number > 0:
    print("This number is positive. Awesome!")
elif number < 0:
    print("This number is negative. Better luck next time!")
else:
    print("Zero it is. A perfect balance!")