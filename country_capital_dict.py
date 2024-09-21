# country_capital_dict.py

# Dictionary of 12 countries and their capitals.
country_capital_dict = {
    'Philippines': 'Manila',
    'Pakistan': 'Islamabad',
    'Romania': 'Burcharest',
    'Paraguay': 'Asuncion',
    'Portugal': 'Lisbon',
    'Syria': 'Damascus',
    'Poland': 'Warsaw',
    'Russia': 'Moscow',
    'Norway': 'Oslo',
    'Oman': 'Muscat',
    'Qatar': 'Doha',   
    'Peru': 'Lima',  
}

# Print the entire dictionary.
print("Country-Capital Dictionary: ", country_capital_dict)

# Access and print the capital of the 5th country.
print()
print("Capital of fifth country 'Portugal': ", country_capital_dict['Portugal'])

# Update the capital of the 8th country.
country_capital_dict['Taiwan'] = 'Taipei'
print()
print("Updated Country-Capital Dictionary: ", country_capital_dict)

# Delete the 11th country from the dictionary.
del country_capital_dict['Qatar']
print("Dictionary after deleting 'Quatar' :", country_capital_dict)

# Print the last key-value pair in the dictionary.
last_country = list(country_capital_dict.items()) [-1]
print()
print("Last key-value pair in the dictionary: ", last_country)