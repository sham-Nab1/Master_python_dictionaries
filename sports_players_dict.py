# sports_players_dict.py

# Dictionary of 10 sports and their most famous players
sports_players_dict = {
    'Volleyball' : 'Alyssa Valdez',
    'Football' : 'Phil Younghusband',
    'Billiards' : 'Efren Reyes',
    'Badminton' : 'Lee Zii Jia',
    'Baseball' : 'Bobby Bonilla',
    'Tennis' : 'Treat Huey',
    'Sepak Takraw' : 'Ruel Tañada',
    'Dragon Boat Racing' : 'Kaye V. Morale',
    'Basketball' : 'Jayson Castro',
    'Gymnastic' : 'Carlos Yul',
}

# Print the entire dictionary.
print("Sports players Dictionary: ", sports_players_dict)

# Access and print the player of the 4th sport.
print()
print("Player of the 4th sport 'Badminton': ", sports_players_dict['Badminton'])

# Update the player of the 6th sport.
sports_players_dict['Tennis'] = 'Alex Eala'
print()
print("Updated Sports Player Dictionary: ", sports_players_dict)

# Delete the 10th sport from the dictionary.
del sports_players_dict['Gymnastic']
print()
print("Dictionary after deleting 'Boxing': ", sports_players_dict)

# Print the last key-value pair in the dictionary.
last_sport = list(sports_players_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_sport)