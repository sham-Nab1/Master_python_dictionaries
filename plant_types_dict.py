# plant_types_dict.py

# Dictionary of 8 plants and their types
plant_types_dict = {
    'Aloe Vera': 'Succulent',
    'Sunflower': 'Flower',
    'Lavender': 'Herb',
    'Daisy': 'Flower',
    'Holly': 'Shrub',
    'Rose': 'Flower',
    'Fern': 'Fern',  
    'Palm': 'Tree' 
}

# Print the entire dictionary
print("Plant Types Dictionary: ", plant_types_dict)

# Access and print the type of the 5th plant
print()
print("Type of the 5th plant 'Holly': ", plant_types_dict['Holly'])

# Update the type of the 2nd plant
plant_types_dict['Sunflower'] = 'Flower (Updated)'
print()
print("Updated Plant Types Dictionary: ", plant_types_dict)

# Delete the 6th plant from the dictionary
del plant_types_dict['Rose']
print()
print("Dictionary after deleting 'Rose': ", plant_types_dict)

# Print the last key-value pair in the dictionary
last_plant = list(plant_types_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_plant)