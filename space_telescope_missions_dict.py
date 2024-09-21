# space_telescope_missions_dict.py

# Dictionary of 5 space telescopes and their missions
space_telescope_missions_dict = {
    'Nikola Tesla Satellite': 'Experimental telecommunications and Earth observation',
    'WISE (Wide-field Infrared Survey Explorer)': 'Mapping the entire sky in infrared',
    'Fermi Gamma-ray Space Telescope': 'Observing gamma rays from cosmic sources',
    'European Space Agency’s Gaia': 'Mapping the Milky Way',  
    'Römer Satellite': 'Studying asteroids and comets'   
}

# Print the entire dictionary
print("Space Telescopes and Their Missions Dictionary: ", space_telescope_missions_dict)

# Access and print the mission of the 3rd telescope
print()
print("Mission of the 3rd telescope 'Fermi Gamma-ray Space Telescope': ", space_telescope_missions_dict['Fermi Gamma-ray Space Telescope'])

# Update the mission of the 1st telescope
space_telescope_missions_dict['Nikola Tesla Satellite'] = 'Experimental telecommunications and Earth observation (Updated)'
print()
print("Updated Space Telescopes Dictionary: ", space_telescope_missions_dict)

# Delete the 4th telescope from the dictionary
del space_telescope_missions_dict['European Space Agency’s Gaia']
print()
print("Dictionary after deleting 'European Space Agency’s Gaia': ", space_telescope_missions_dict)

# Print the last key-value pair in the dictionary
last_telescope = list(space_telescope_missions_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_telescope)
