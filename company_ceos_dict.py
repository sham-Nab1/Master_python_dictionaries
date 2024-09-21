# company_ceos_dict.py

# Dictionary of 10 companies and their current CEOs
company_ceos_dict = {
    'Apple': 'Tim Cook',
    'Google': 'Sundar Pichai',
    'Microsoft': 'Satya Nadella',
    'Amazon': 'Andy Jassy',
    'Facebook': 'Mark Zuckerberg',
    'Tesla': 'Elon Musk',
    'IBM': 'Arvind Krishna',
    'Oracle': 'Safra Catz',
    'Spotify': 'Daniel Ek',
    'Adobe': 'Shantanu Narayen'
}

# Print the entire dictionary
print("Company CEOs Dictionary: ", company_ceos_dict)

# Access and print the CEO of the 6th company
print()
print("CEO of the 6th company (Tesla): ", company_ceos_dict['Tesla'])

# Update the CEO of the 3rd company
company_ceos_dict['Microsoft'] = 'Brad Smith'
print()
print("Updated Company CEOs Dictionary: ", company_ceos_dict)

# Delete the 9th company from the dictionary
del company_ceos_dict['Spotify']
print()
print("Dictionary after deleting 'Spotify': ", company_ceos_dict)

# Print the last key-value pair in the dictionary
last_company = list(company_ceos_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_company)
