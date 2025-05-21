# Ask the User's Age
age = int(input("How old are you? "))

X = 18 - age

# Decide the Eligibility
if age >= 18:
    print("Congratulations! You are eligible to vote. Go make a difference!")
else:
    print("Oops! You’re not eligible yet. But hey, only " + str(X) + " more years to go!")