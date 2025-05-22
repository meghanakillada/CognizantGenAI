# Input the Password
password = input("Enter a password: ")

# Evaluate the Password
is_long = len(password) >= 8
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(char in "!@#$%^&*()-_+=<>?{}[]|:;\"'`~" for char in password)
feedback = []

if not is_long:
    feedback.append("at least 8 characters")
if not has_upper:
    feedback.append("one uppercase letter")
if not has_lower:
    feedback.append("one lowercase letter")
if not has_digit:
    feedback.append("one digit")
if not has_special:
    feedback.append("one special character")

if not feedback:
    print("Your password is strong!💪")
else:
    message = "Your password needs" + ", ".join(feedback[:-1])
    if len(feedback) > 1:
        message += " and " + feedback[-1]
    print(message + ".")