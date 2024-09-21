# technology_inventors_dict.py

# Dictionary of 6 technologies and their inventors
technology_inventors_dict = {
    'Telephone': 'Alexander Graham Bell',
    'Camera': 'Joseph Nicéphore Niépce',
    'Microwave Oven': 'Percy Spencer',
    'Television': 'John Logie Baird',
    'Light Bulb': 'Thomas Edison',
    'Computer': 'Charles Babbage',
}

# Print the entire dictionary
print("Technology Inventors Dictionary: ", technology_inventors_dict)

# Access and print the inventor of the 4th technology
print()
print("Inventor of the 4th technology 'Television': ", technology_inventors_dict['Television'])

# Update the inventor of the 2nd technology
technology_inventors_dict['Camera'] = 'Thomas Alva Edison'
print()
print("Updated Technology Inventors Dictionary: ", technology_inventors_dict)

# Delete the 6th technology from the dictionary
del technology_inventors_dict['Computer']
print()
print("Dictionary after deleting 'Computer': ", technology_inventors_dict)

# Print the last key-value pair in the dictionary
last_technology = list(technology_inventors_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_technology)