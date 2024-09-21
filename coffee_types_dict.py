# coffee_types_dict.py

# Dictionary of 10 types of coffee and their descriptions
coffee_types_dict = {
    'Espresso': 'A strong and concentrated coffee brewed by forcing hot water through finely-ground coffee.',
    'Americano': 'Espresso mixed with hot water, resulting in a similar strength to drip coffee.',
    'Latte': 'Espresso combined with steamed milk and topped with a small amount of milk foam.',
    'Cappuccino': 'Espresso with equal parts steamed milk and milk foam, often dusted with cocoa powder.',
    'Macchiato': 'Espresso with a small amount of foamed milk on top.',
    'Mocha': 'A chocolate-flavored variant of a latte, combining espresso, steamed milk, and chocolate syrup.',
    'Flat White': 'A coffee drink consisting of espresso and microfoam, popular in Australia and New Zealand.',
    'Cold Brew': 'Coffee brewed with cold water over an extended period, resulting in a smooth flavor.',
    'Affogato': 'A dessert-style coffee made by pouring a shot of hot espresso over a scoop of ice cream.',
    'Ristretto': 'A short shot of espresso made with the same amount of coffee but less water.',
}

# Print the entire dictionary
print("Coffee Types Dictionary: ", coffee_types_dict)

# Access and print the description of the 4th type of coffee
print()
print("Description of the 4th type of coffee (Cappuccino): ", coffee_types_dict['Cappuccino'])

# Update the description of the 8th type of coffee
coffee_types_dict['Cold Brew'] = 'Coffee steeped in cold water for an extended period, yielding a smooth, less acidic flavor.'
print()
print("Updated Coffee Types Dictionary: ", coffee_types_dict)

# Delete the 5th type of coffee from the dictionary
del coffee_types_dict['Mocha']
print()
print("Dictionary after deleting 'Mocha': ", coffee_types_dict)

# Print the last key-value pair in the dictionary
last_coffee = list(coffee_types_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_coffee)
