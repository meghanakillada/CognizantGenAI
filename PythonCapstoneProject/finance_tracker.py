expenses_dict = {}

# Add expenses
def add_expense(category, description, amount):
    expense = (description, amount)
    if category in expenses_dict:
        expenses_dict[category].append(expense)
    else:
        expenses_dict[category] = [expense]
    print(f"Expense added successfully.")

# View all expenses
def view_expenses(data):
    if not data:
        print("No expenses recorded.")
        return
    print("\nExpenses:")
    for category, expenses in data.items():
        print(f"Category: {category}")
        for expense in expenses:
            print(f"  - {expense[0]}: ${expense[1]}")

# View summary by category
def view_summary(data):
    if not data:
        print("No expenses recorded.")
        return
    print("\nSummary:")
    for category, expenses in data.items():
        total = sum(float(expense[1]) for expense in expenses)
        print(f"Category: {category}, Total: ${total:.2f}")

# Set up the project
def menu():
    while True:
        try:
            print("\nWhat would you like to do?:")
            print("1. Add Expense")
            print("2. View All Expenses")
            print("3. View Summary")
            print("4. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                description = input("Enter expense description: ")
                if not description:
                    raise ValueError("Description cannot be empty.")
                category = input("Enter category: ")
                if not category:
                    raise ValueError("Category cannot be empty.")
                try:
                    amount = float(input("Enter amount: "))
                except ValueError:
                    print("Invalid amount. Please enter a numeric value.")
                    continue
                if not amount:
                    raise ValueError("Amount cannot be empty.")
                add_expense(category, description, amount)
            elif choice == '2':
                view_expenses(expenses_dict)
            elif choice == '3':
                view_summary(expenses_dict)
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        # Handle exceptions
        except ValueError as ve:
            print(f"Input Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

print("Welcome to the Personal Finance Tracker!")
menu()