# product_prices_dict.py

# Dictionary of 10 products and their prices
product_prices_dict = {
    'Smartphone': 699.99,
    'Headphones': 199.99,
    'Smartwatch': 249.99,
    'Printer': 129.99,
    'Monitor': 299.99,
    'Keyboard': 79.99,
    'Laptop': 999.99,    
    'Tablet': 329.99,
    'Camera': 499.99,   
    'Mouse': 49.99,
}

# Print the entire dictionary
print("Product Prices Dictionary: ", product_prices_dict)

# Access and print the price of the 4th product
print()
print("Price of the 4th product 'Printer': ", product_prices_dict['Printer'])

# Update the price of the 9th product
product_prices_dict['Camera'] = 89.99
print()
print("Updated Product Prices Dictionary: ", product_prices_dict)

# Delete the 6th product from the dictionary
del product_prices_dict['Keyboard']
print()
print("Dictionary after deleting 'Keyboard': ", product_prices_dict)

# Print the last key-value pair in the dictionary
last_product = list(product_prices_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_product)