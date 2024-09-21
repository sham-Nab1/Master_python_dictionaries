# space_missions_dict.py

# Dictionary of 5 space missions and their corresponding years
space_missions_dict = {
    'James Webb Space Telescope': 2021,
    'Space Shuttle Discovery': 1984,
    'Mars Rover Opportunity': 2004,
    'Apollo 11': 1969,
    'Voyager 1': 1977,   
}

# Print the entire dictionary
print("Space Missions Dictionary: ", space_missions_dict)

# Access and print the year of the 3rd mission
print()
print("Year of the 3rd mission (Mars Rover Opportunity): ", space_missions_dict['Mars Rover Opportunity'])

# Update the year of the 2nd mission
space_missions_dict['Voyager 1'] = 1978
print()
print("Updated Space Missions Dictionary: ", space_missions_dict)

# Delete the 4th mission from the dictionary
del space_missions_dict['Mars Rover Opportunity']
print()
print("Dictionary after deleting 'Mars Rover Opportunity': ", space_missions_dict)

# Print the last key-value pair in the dictionary
last_mission = list(space_missions_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_mission)