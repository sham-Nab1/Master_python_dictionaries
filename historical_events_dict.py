# historical_events_dict.py

# Dictionary of 8 historical events and their years
historical_events_dict = {
    'Declaration of Independence': 1898,
    'Martial Law Declaration': 1972,
    'People Power Revolution': 1986,
    'Philippine Revolution': 1896,
    'Spanish Colonization': 1565,
    'American Occupation': 1898,
    'Commonwealth Act': 1935,
    'World War II': 1941   
}

# Print the entire dictionary
print("Historical Events Dictionary: ", historical_events_dict)

# Access and print the year of the 2nd event
print()
print("Year of the 2nd event 'Martial Law Declaration': ", historical_events_dict['Martial Law Declaration'])

# Update the year of the 7th event
historical_events_dict['Commonwealth Act'] = 1973
print()
print("Updated Historical Events Dictionary: ", historical_events_dict)

# Delete the 5th event from the dictionary
del historical_events_dict['Spanish Colonization']
print()
print("Dictionary after deleting 'Spanish Colonization': ", historical_events_dict)

# Print the last key-value pair in the dictionary
last_event = list(historical_events_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_event)