# sports_events_dict.py

# Dictionary of 7 sports events and their corresponding years
sports_events_dict = {
    'Tour de France': 2021,
    'FIFA World Cup': 2018,
    'NBA Finals': 2021,
    'Super Bowl': 2022,
    'Wimbledon': 2021,
    'Olympics': 2021,    
    'US Open': 2021
}

# Print the entire dictionary
print("Sports Events Dictionary: ", sports_events_dict)

# Access and print the year of the 3rd sports event
print()
print("Year of the 3rd sports event 'NBA Finals': ", sports_events_dict['NBA Finals'])

# Update the year of the 6th sports event
sports_events_dict['Olympics'] = 2022
print()
print("Updated Sports Events Dictionary: ", sports_events_dict)

# Delete the 5th sports event from the dictionary
del sports_events_dict['Wimbledon']
print()
print("Dictionary after deleting 'Wimbledon': ", sports_events_dict)

# Print the last key-value pair in the dictionary
last_event = list(sports_events_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_event)
