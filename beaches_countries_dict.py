# beaches_countries_dict.py

# Dictionary of 8 beaches and the countries they are located in
beaches_countries_dict = {
    'Anse Source d\'Argent': 'Seychelles',
    'Jumeirah Beach': 'UAE',
    'Kuta Beach': 'Indonesia',
    'Surfers Paradise': 'Australia',
    'Varadero Beach': 'Cuba',
    'Seven Mile Beach': 'Jamaica',
    'Ipanema Beach': 'Brazil',
    'Cannon Beach': 'USA',
    'Tulum Beach': 'Mexico'
}

# Print the entire dictionary
print("Beaches Countries Dictionary: ", beaches_countries_dict)

# Access and print the country of the 3rd beach
print()
print("Country of the 3rd beach 'Kuta Beach': ", beaches_countries_dict['Kuta Beach'])

# Update the country of the 6th beach
beaches_countries_dict['Seven Mile Beach'] =  'Jamaica (Updated)'
print()
print("Updated Beaches Countries Dictionary: ", beaches_countries_dict)

# Delete the 5th beach from the dictionary
del beaches_countries_dict['Varadero Beach']
print()
print("Dictionary after deleting 'Varadero Beach': ", beaches_countries_dict)

# Print the last key-value pair in the dictionary
last_beach = list(beaches_countries_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_beach)
