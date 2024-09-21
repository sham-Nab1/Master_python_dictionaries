# river_lengths_dict.py

# Dictionary of 6rivers and their lengths in kilometers
river_lengths_dict = {
    'Mississippi': 3730,
    'Yellow River':5464,
    'Ob River': 5410,
    'Parana': 4880,
    'Amazon': 6400,
    'Nile': 6650
}

# Print the entire dictionary
print("River Lengths Dictionary: ", river_lengths_dict)

# Access and print the length of the 2nd river
print()
print("Length of the 2nd river 'Yellow River': ", river_lengths_dict['Yellow River'])

# Update the length of the 5th river
river_lengths_dict['Amazon'] = 5600
print()
print("Updated River Lengths Dictionary: ", river_lengths_dict)

# Delete the 4th river from the dictionary
del river_lengths_dict['Parana']
print()
print("Dictionary after deleting 'Parana': ", river_lengths_dict)

# Print the last key-value pair in the dictionary
last_river = list(river_lengths_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_river)