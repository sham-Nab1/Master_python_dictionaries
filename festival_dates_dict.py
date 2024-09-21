# festival_dates_dict.py

# Dictionary of 10 festivals in the Philippines and their celebration dates
festival_dates_dict = {
    'Pintados-Kasadyaan Festival': 'June 29',
    'Obando Fertility Rites': 'May 17-19',
    'Mooncake Festival': 'September 29',
    'Ati-Atihan Festival': 'January 20',
    'Panagbenga Festival': 'February 1',
    'Kadayawan Festival': 'August 15',
    'Sinulog Festival': 'January 15',
    'Banggka Festival': 'April 8',
    'Parada ng Lechon': 'June 24',  
    'Pahiyas Festival': 'May 15',
}

# Print the entire dictionary
print("Festival Dates Dictionary: ", festival_dates_dict)

# Access and print the date of the 3rd festival
print()
print("Date of the 3rd festival 'Mooncake Festival': ", festival_dates_dict['Mooncake Festival'])

# Update the date of the 7th festival
festival_dates_dict['Sinulog Festival'] = 'April 9'
print()
print("Updated Festival Dates Dictionary: ", festival_dates_dict)

# Delete the 5th festival from the dictionary
del festival_dates_dict['Panagbenga Festival']
print()
print("Dictionary after deleting 'Panagbenga Festival': ", festival_dates_dict)

# Print the last key-value pair in the dictionary
last_festival = list(festival_dates_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_festival)