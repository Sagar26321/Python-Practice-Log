# Task: Create a dictionary representing a Product in a store.

# The dictionary variable name should be product.

# It needs these keys: "name" (String), "price" (Float), and "in_stock" (Boolean).

# After creating it, write code that decreases the price by 10% (math operation).

# Print the new price.

product =  {
    "name" : "Television",
    "price" : 50000.0,
    "in_stock" : True
}
product["price"] = product["price"] * 0.9
print("The new price is:", product["price"])

