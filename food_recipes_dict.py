# food_recipes_dict.py

# Dictionary of 8 foods and their recipes
food_recipes_dict = {
    'Adobo': 'Marinate chicken or pork in soy sauce, vinegar, garlic, and spices, then simmer until tender.',
    'Sinigang': 'Cook pork or shrimp with tamarind, tomatoes, and vegetables in a sour broth.',
    'Lechon': 'Roast a whole pig over charcoal until the skin is crispy and golden brown.',
    'Pancit Canton': 'Stir-fry noodles with vegetables, meat, and soy sauce.',
    'Lumpia': 'Wrap vegetables and meat in thin pastry and deep-fry until golden.',
    'Kare-Kare': 'Prepare oxtail in a thick peanut sauce with vegetables.',
    'Halo-Halo': 'Layer shaved ice with sweet beans, fruits, and leche flan, topped with ube.',
    'Puto': 'Steam rice flour mixed with sugar and coconut milk in small cups.',
}

# Print the entire dictionary
print("Food Recipes Dictionary: ", food_recipes_dict)

# Access and print the recipe of the 5th food
print()
print("Recipe of the 5th food (Kare-Kare): ", food_recipes_dict['Kare-Kare'])

# Update the recipe of the 3rd food
food_recipes_dict['Lechon'] = 'Marinate a whole pig, then roast over an open flame until crispy.'
print()
print("Updated Food Recipes Dictionary: ", food_recipes_dict)

# Delete the 7th food from the dictionary
del food_recipes_dict['Halo-Halo']
print()
print("Dictionary after deleting 'Halo-Halo': ", food_recipes_dict)

# Print the last key-value pair in the dictionary
last_food = list(food_recipes_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_food)