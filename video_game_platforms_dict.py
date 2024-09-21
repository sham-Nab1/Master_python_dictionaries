# video_game_platforms_dict.py

# Dictionary of 8 video games and their platforms
video_game_platforms_dict = {
    'Red Dead Redemption 2': 'PC, PS4, Xbox One',
    'Apex Legends': 'PC, PS4, Xbox One, Switch',
    'Super Mario Odyssey': 'Nintendo Switch',
    'Overwatch': 'PC, PS4, Xbox One, Switch',
    'Dark Souls III': 'PC, PS4, Xbox One',
    'Stardew Valley': 'Multi-platform',
    'Minecraft': 'Multi-platform',  
    'God of War': 'PS4',
}

# Print the entire dictionary
print("Video Game Platforms Dictionary: ", video_game_platforms_dict)

# Access and print the platform of the 2nd video game
print()
print("Platform of the 2nd video game 'Apex Legends': ", video_game_platforms_dict['Apex Legends'])

# Update the platform of the 6th video game
video_game_platforms_dict['Stardew Valley'] = 'Multi-platform'
print()
print("Updated Video Game Platforms Dictionary: ", video_game_platforms_dict)

# Delete the 4th video game from the dictionary
del video_game_platforms_dict['Overwatch']
print()
print("Dictionary after deleting 'Overwatch': ", video_game_platforms_dict)

# Print the last key-value pair in the dictionary
last_game = list(video_game_platforms_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_game)