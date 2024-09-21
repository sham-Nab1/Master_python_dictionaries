# animal_habitats_dict.py

# # Dictionary of 8 animals and their natural habitats
animal_habitats_dict = {
    'Red Fox' : 'Forest and grassland',
    'Grizzly Bear' : 'Mountain forests',
    'Panda' : 'Bamboo forest',
    'Cheetah' : 'Grassland',
    'Kangaroo' : 'Bushland',
    'Elephant:' : 'Grassland',
    'Penguin' : 'Antarctic',
    'Polar Bear' : 'Arctic',
}

# Print the entire dictionary
print("Animal Habitats Dictionary: ", animal_habitats_dict)

# Access and print the habitat of the 3rd animal
print()
print("Habitat of the 3rd animal 'Panda': ", animal_habitats_dict['Panda'])

# Update the habitat of the 5th animal
animal_habitats_dict['Kangaroo'] = 'Outback'
print()
print("Updated Animal Habitats Dictionary: ", animal_habitats_dict)

# Delete the 7th animal from the dictionary
del animal_habitats_dict['Penguin']
print()
print("Dictionary after deleting 'Penguin': ", animal_habitats_dict)

# Print the last key-value pair in the dictionary
last_animal = list(animal_habitats_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_animal)