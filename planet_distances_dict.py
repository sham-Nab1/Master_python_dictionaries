 # planet_distances_dict.py

 # Dictionary of 8 planets and their distances from the sun (in million kilometers)
planet_distances_dict = {
    'Mercury': 57.91,
    'Venus': 108.2,
    'Earth': 149.6,
    'Mars': 227.9,
    'Jupiter': 778.5,
    'Saturn': 1427,
    'Uranus': 2871,
    'Neptune': 4497.1
}

# Print the entire dictionary
print("Planet Distances Dictionary: ", planet_distances_dict)

# Access and print the distance of the 3rd planet
print()
print("Distance of the 3rd planet (Earth): ", planet_distances_dict['Earth'])

# Update the distance of the 5th planet
planet_distances_dict['Jupiter'] = 778.6
print()
print("Updated Planet Distances Dictionary: ", planet_distances_dict)

# Delete the 7th planet from the dictionary
del planet_distances_dict['Uranus']
print()
print("Dictionary after deleting 'Uranus': ", planet_distances_dict)

# Print the last key-value pair in the dictionary
last_planet = list(planet_distances_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_planet)