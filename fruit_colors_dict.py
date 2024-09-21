# fruit_colors_dict.py

# Dictionary of 8 fruits and their corresponding colors.
fruit_colors_dict = {
    'Blackberry' : 'Black',
    'Watermelon' : 'Green/Pink',  
    'Strawberry' : 'Red',
    'Peach' : 'Pink',
    'Mango' : 'Yellow',
    'Kiwi' : 'Green',
    'Orange' : 'Orange',
    'Grape' : 'Purple',
}
# Print the entire dictionary.
print("Fruit Colors Dictionary: ", fruit_colors_dict)

# Access and print the color of the 6th fruit.
print()
print("Color of the 6th fruit: ", fruit_colors_dict['Kiwi'])

# Update the color of the 4th fruit.
fruit_colors_dict['Peach'] = 'Yellow'
print()
print("Updated Fruit Colors Dictionary: ", fruit_colors_dict)

# Delete the 7th fruit from the dictionary.
del fruit_colors_dict['Orange']
print()
print("Dictionary after deleting Kiwi: ", fruit_colors_dict)

# Print the last key-value pair in the dictionary.
last_fruit = list(fruit_colors_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_fruit)