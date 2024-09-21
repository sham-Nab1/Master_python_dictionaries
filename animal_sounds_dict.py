# animal_sounds_dict.py

# Dictionary of 8 animals and their corresponding sounds.
animal_sounds_dict = {
    'Dog': 'Bark',
    'Bird': 'Chirp',
    'Lion': 'Roar',
    'Frog': 'Ribbit',
    'Duck': 'Quack',
    'Sheep': 'Baa',
    'Cow': 'Moo',
    'Cat': 'Meow'
}

# Print the entire dictionary.
print("Animal Sounds Dictionary: ", animal_sounds_dict)

# Access and print the sound of the 4th animal.
print()
print("Sound of fourth animal: ", animal_sounds_dict['Frog'])

# Update the sound of the 7th animal.
animal_sounds_dict['Lion'] = 'Growl'
print("Updated Animal Sound Dictionary: ", animal_sounds_dict)

# Delete the 5th animal from the dictionary.
del animal_sounds_dict['Duck']
print()
print("Dictionary after deleting 'Duck': ", animal_sounds_dict)

# Print the last key-value pair in the dictionary.
last_animal = list(animal_sounds_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_animal)