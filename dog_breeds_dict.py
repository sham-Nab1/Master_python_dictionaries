# dog_breeds_dict.py

# Dictionary of 10 dog breeds and their sizes
dog_breeds_dict = {
    'Labrador Retriever': 'Large',
    'Golden Retriever': 'Large',
    'Siberian Husky': 'Large',
    'Rottweiler': 'Large',
    'Chihuahua': 'Small',
    'Bulldog': 'Medium',
    'Shih Tzu': 'Small',
    'Poodle': 'Medium',
    'Beagle': 'Medium', 
    'Boxer': 'Large',   
}

# Print the entire dictionary
print("Dog Breeds Dictionary: ", dog_breeds_dict)

# Access and print the size of the 5th breed
print()
print("Size of the 5th breed 'Chihuahua': ", dog_breeds_dict['Chihuahua'])

# Update the size of the 8th breed
dog_breeds_dict['Poodle'] = 'Large'
print()
print("Updated Dog Breeds Dictionary: ", dog_breeds_dict)

# Delete the 6th breed from the dictionary
del dog_breeds_dict['Bulldog']
print()
print("Dictionary after deleting 'Bulldog': ", dog_breeds_dict)

# Print the last key-value pair in the dictionary
last_breed = list(dog_breeds_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_breed)