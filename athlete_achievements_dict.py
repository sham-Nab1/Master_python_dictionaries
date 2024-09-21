# athlete_achievements_dict.py

# Dictionary of 8 Filipino athletes and their greatest achievements
athlete_achievements_dict = {
    'Nesthy Petecio': 'Silver Medal in Womens Featherweight at the 2020 Tokyo Olympics',
    'Carlos Yulo': 'Gold Medal in Floor Exercise at the 2019 World Championships',
    'Hidilyn Diaz': 'Gold Medal in Weightlifting at the 2020 Tokyo Olympics',
    'Elma Muros-Posadas': '8-time SEA Games Gold Medalist in Athletics',
    'Milo Rivera': 'First Filipino to win the GRC Formula Championship',
    'Mika Reyes': 'Gold Medal in Volleyball at the 2015 SEA Games',
    'Rugby 7s Team': 'Bronze Medal at the 2019 SEA Games',
    'Manny Pacquiao': '8-Division World Champion',
}

# Print the entire dictionary
print("Athlete Achievements Dictionary: ", athlete_achievements_dict)

# Access and print the achievement of the 5th athlete
print()
print("Achievement of the 5th athlete 'Milo Rivera': ", athlete_achievements_dict['Milo Rivera'])

# Update the achievement of the 3rd athlete
athlete_achievements_dict['Hidilyn Diaz'] = 'Gold Medal in Weightlifting at the 2022 Japan Olympics'
print()
print("Updated Athlete Achievements Dictionary: ", athlete_achievements_dict)

# Delete the 7th athlete from the dictionary
del athlete_achievements_dict['Rugby 7s Team']
print()
print("Dictionary after deleting 'Rugby 7s Team': ", athlete_achievements_dict)

# Print the last key-value pair in the dictionary
last_athlete = list(athlete_achievements_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_athlete)