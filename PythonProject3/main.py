# Input the Password
password = input("Enter a password: ")

# Evaluate the Password
is_long = len(password) >= 8
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(char in "!@#$%^&*()-_+=<>?{}[]|:;\"'`~" for char in password)
feedback = []
strength = 10
if not is_long:
    strength -= 2
    feedback.append("at least 8 characters")
if not has_upper:
    strength -= 2
    feedback.append("one uppercase letter")
if not has_lower:
    strength -= 2
    feedback.append("one lowercase letter")
if not has_digit:
    strength -= 2
    feedback.append("one digit")
if not has_special:
    strength -= 2
    feedback.append("one special character")
print(f"Password strength: {strength}/10", end=" ")
if not feedback:
    print("Your password is strong!💪")
else:
    message = "Your password needs" + ", ".join(feedback[:-1])
    if len(feedback) > 1:
        message += " and " + feedback[-1]
    print(message + ".")