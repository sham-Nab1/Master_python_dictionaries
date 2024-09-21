# festival_locations_dict.py

# Dictionary of 8 festivals and their locations
festival_locations_dict = {
    'Sinulog': 'Cebu City',
    'Ati-Atihan': 'Kalibo, Aklan',
    'Pahiyas': 'Lucban, Quezon',
    'Panagbenga': 'Baguio City',
    'Kadayawan': 'Davao City',
    'Obando Fertility Rites': 'Obando, Bulacan',
    'Manggahan Festival': 'Guimaras',
    'Feast of the Black Nazarene': 'Quiapo, Manila'
}

# Print the entire dictionary
print("Festival Locations Dictionary: ", festival_locations_dict)

# Access and print the location of the 4th festival
print()
print("Location of the 4th festival (Panagbenga): ", festival_locations_dict['Panagbenga'])

# Update the location of the 6th festival
festival_locations_dict['Obando Fertility Rites'] = 'Obando, Bulacan (Updated Location)'
print()
print("Updated Festival Locations Dictionary: ", festival_locations_dict)

# Delete the 2nd festival from the dictionary
del festival_locations_dict['Ati-Atihan']
print()
print("Dictionary after deleting 'Ati-Atihan': ", festival_locations_dict)

# Print the last key-value pair in the dictionary
last_festival = list(festival_locations_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_festival)
