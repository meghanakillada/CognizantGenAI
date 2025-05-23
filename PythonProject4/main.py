# Create the Inventory
inventory ={
"apple": (10, 2.5),
"banana": (20, 1.2),
}


# Display the Inventory
def display_inventory(inventory):
    for item, (quantity, price) in inventory.items():
        print(f"Item: {item}, Quantity: {quantity}, Price: ${price:.2f}")

print("Current Inventory:")
display_inventory(inventory)

# Add, Remove. and Update Items
inventory["mango"] = (15, 3.0)
del inventory["banana"]
inventory["apple"] = (12, 2.8)

# Calculate Total Value
def calculate_total_value(inventory):
    print("Total value of inventory: ", end="")
    total_value = 0
    for item, (quantity, price) in inventory.items():
        total_value += quantity * price
    print(total_value)

print("Updated Inventory:")
display_inventory(inventory)
calculate_total_value(inventory)