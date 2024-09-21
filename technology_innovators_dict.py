# technology_innovators_dict.py

# Dictionary of 8 technologies and their innovators
technology_innovators_dict = {
    'Raspberry Pi': 'Eugene M. De Leon',
    'Sustainable Energy': 'Josefina S. C. Lacson',
    'Mobile Apps': 'Manny J. Pangilinan',
    'Telecommunication Systems': 'Francisco C. Tatad',
    'E-Learning Platforms': 'Dr. Liza A. B. Alano',
    'AgriTech Solutions': 'Ronald L. R. Yu',
    'Smart Farming': 'Ma. Cynthia J. L. Calinisan',
    'HealthTech Innovations': 'Dr. Raul A. R. Cordero'
}

# Print the entire dictionary
print("Technology Innovators Dictionary: ", technology_innovators_dict)

# Access and print the innovator of the 4th technology
print()
print("Innovator of the 4th technology 'Telecommunication Systems': ", technology_innovators_dict['Telecommunication Systems'])

# Update the innovator of the 2nd technology
technology_innovators_dict['Sustainable Energy'] = 'Dr. Maria A. P. Mendoza'
print()
print("Updated Technology Innovators Dictionary: ", technology_innovators_dict)

# Delete the 6th technology from the dictionary
del technology_innovators_dict['AgriTech Solutions']
print()
print("Dictionary after deleting 'AgriTech Solutions': ", technology_innovators_dict)

# Print the last key-value pair in the dictionary
last_tech = list(technology_innovators_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_tech)
