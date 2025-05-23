# Task 1 Working with Lists
fruits = ["apple", "banana", "blueberry", "mango", "watermelon"]
print("Original list:", fruits)
fruits.append("orange")
print("After adding a fruit:", fruits)
fruits.remove("apple")
print("After removing a fruit:", fruits)
print("Reversed list:", fruits[::-1])

# Task 2 Exploring Dictionaries
info = {"name": "Maggie Killada", "age": 20, "city": "San Diego"}
info["favorite color"] = "Coral"
info["city"] = "Los Angeles"
print("Keys:", end=" ")
for key in info.keys():
    print(f"{key}", end=" ")
print("\nValues:", end=" ")
for value in info.values():
    print(f"{value}", end=" ")

# Task 3 Using Tuples
favorite_things = ("Interstellar","Positions","Hunger Games")
try:
    favorite_things[0] = 'The Matrix'
except TypeError:
    print("\nOops! Tuples cannot be changed.")
print(f"Length of tuple: {len(favorite_things)}")