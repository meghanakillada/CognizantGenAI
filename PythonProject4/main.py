# Create the Inventory
inventory ={
"apple": (10, 2.5),
"banana": (20, 1.2),
}

# Display the Inventory
print("Current Inventory:")
for item, (quantity, price) in inventory.items():
    print(f"Item: {item}, Quantity: {quantity}, Price: ${price:.2f}")

# Add, Remove. and Update Items
inventory["mango"] = (15, 3.0)
del inventory["banana"]
inventory["apple"] = (12, 2.8)

print("Updated Inventory:")
for item, (quantity, price) in inventory.items():
    print(f"Item: {item}, Quantity: {quantity}, Price: ${price:.2f}")
print("Total value of inventory: ", end="")
total_value = 0
for item, (quantity, price) in inventory.items():
    total_value += quantity * price
print(f"${total_value:.2f}")