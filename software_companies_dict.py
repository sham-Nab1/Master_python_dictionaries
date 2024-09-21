# software_companies_dict.py

# Dictionary of 10 software companies and their headquarters.
software_companies_dict = {
    'Salesforce': 'San Francisco, California, USA',   
    'Salesforce': 'San Francisco, California, USA',
    'Google': 'Mountain View, California, USA',
    'Intuit': 'Mountain View, California, USA',
    'Apple': 'Cupertino, California, USA',
    'Adobe': 'San Jose, California, USA',
    'IBM': 'Armonk, New York, USA',
    'Oracle': 'Austin, Texas, USA',
    'Spotify': 'Stockholm, Sweden',
    'SAP': 'Walldorf, Germany'
}

# Print the entire dictionary
print("Software Companies Dictionary: ", software_companies_dict)

# Access and print the headquarters of the 3rd company.
print()
print("Headquarters of the 3rd company: ", software_companies_dict['Google'])

# Update the headquarters of the 8th company.
software_companies_dict['Oracle'] = 'San Francisco, California, USA (Updated)'
print()
print("Updated Software Companies Dictionary: ", software_companies_dict)

# Delete the 9th company from the dictionary.
del software_companies_dict['Spotify']
print()
print("Dictionary after deleting 'Spotify': ", software_companies_dict)

# Print the last key-value pair in the dictionary.
last_company = list(software_companies_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_company)