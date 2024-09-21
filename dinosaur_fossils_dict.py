# dinosaur_fossils_dict.py

# Dictionary of 7 dinosaurs and where their fossils were found
dinosaur_fossils_dict = {
    'Tyrannosaurus Rex': 'North America',
    'Triceratops': 'North America',
    'Velociraptor': 'Mongolia',
    'Brachiosaurus': 'North America',
    'Stegosaurus': 'North America',
    'Spinosaurus': 'North Africa',
    'Allosaurus': 'North America'
}

# Print the entire dictionary
print("Dinosaur Fossils Dictionary: ", dinosaur_fossils_dict)

# Access and print the location of the 4th dinosaur's fossils
print()
print("Location of the 4th dinosaur's fossils (Brachiosaurus): ", dinosaur_fossils_dict['Brachiosaurus'])

# Update the location of the 2nd dinosaur's fossils
dinosaur_fossils_dict['Triceratops'] = 'United States'
print()
print("Updated Dinosaur Fossils Dictionary: ", dinosaur_fossils_dict)

# Delete the 6th dinosaur from the dictionary
del dinosaur_fossils_dict['Spinosaurus']
print()
print("Dictionary after deleting 'Spinosaurus': ", dinosaur_fossils_dict)

# Print the last key-value pair in the dictionary
last_dinosaur = list(dinosaur_fossils_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_dinosaur)
