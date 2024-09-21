# state_capitals_dict.py

# Dictionary of 1 states and their capitals
state_capitals_dict = {
    'California': 'Sacramento',
    'North Carolina': 'Raleigh',
    'Florida': 'Tallahassee',
    'Washington': 'Olympia',
    'Virginia': 'Richmond',
    'New York': 'Albany',
    'Georgia': 'Atlanta',
    'Arizona': 'Phoenix',
    'Ohio': 'Columbus',
    'Texas': 'Austin',
}    

# Print the entire dictionary
print("State Capitals Dictionary: ", state_capitals_dict)

# Access and print the capital of the 4th state
print()
print("Capital of the 4th state 'Washington': ", state_capitals_dict['Washington'])

# Update the capital of the 9th state
state_capitals_dict['Ohio'] = 'Columbus'
print()
print("Updated State Capitals Dictionary: ", state_capitals_dict)

# Delete the 7th state from the dictionary
del state_capitals_dict['Georgia']
print()
print("Dictionary after deleting 'Georgia': ", state_capitals_dict)

# Print the last key-value pair in the dictionary
last_state = list(state_capitals_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_state)
