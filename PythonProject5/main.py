import turtle

# Factorial Function
def factorial(n):
    """Returns the factorial of n using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Fibonacci Function
def fibonacci(n):
    """Returns the nth Fibonacci number using recursion."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
# Recursive Fractal Pattern
def fractal(depth):
    """Draws a simple fractal tree pattern using turtle recursion."""
    if depth == 0:
        return
    else:
        turtle.forward(100)
        turtle.right(30)
        fractal(depth - 1)
        turtle.left(60)
        fractal(depth - 1)
        turtle.right(30)
        turtle.backward(100)

# Menu of Recursive Functions
print("Welcome to the Recursive Artistry Program! Choose an option:", end=" ")
while True:
    option = input("1. Calculate Factorial 2. Find Fibonacci 3. Draw a Recursive Fractal 4. Exit: ")
    if option == "1":
        factorial_num = int(input("Enter a number to find its factorial: "))
        if factorial_num <= 0:
            print("Enter a positive value.")
            continue
        factorial(factorial_num)
    elif option == "2":
        fibonacci_num = int(input("Enter the position of the Fibonacci number: "))
        if fibonacci_num <= 0:
            print("Enter a positive value.")
            continue
        fibonacci(fibonacci_num)
    elif option == "3":
        fractal_depth = int(input("Enter the depth for the fractal pattern (1-9): "))
        if fractal_depth <= 0:
            print("Enter a positive value.")
            continue
        turtle.reset()
        turtle.title("Recursive Fractal Pattern")
        turtle.setworldcoordinates(-300, -300, 300, 300)
        turtle.penup()
        turtle.goto(0, -250)
        turtle.setheading(90)
        turtle.pendown()
        turtle.speed(0)
        fractal(fractal_depth)
        screen = turtle.Screen()
        screen.exitonclick()
    elif option == "4":
        break
    # User-Friendly Program
    else:
        print("Invalid option. Please choose a valid option.")