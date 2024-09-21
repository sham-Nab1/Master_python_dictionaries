# movie_directors_dict.py

# Dictionary of 10 movies and their directors in the Philippines.
movie_directors_dict = {
    'Kita Kita': 'Sigrid Andrea P. P. C. Bernardo',
    'Ang Babae sa Septic Tank': 'Marlo R. Mortel',
    'Goyo: Ang Batang Heneral': 'Jerrold Tarog',
    'The Hows of Us': 'Cathy Garcia-Molina',
    'Deadma Walking': 'Julio Castillo',
    'Heneral Luna': 'Jerrold Tarog',  
    'Barber Tales': 'Miko Livelo',
    'On the Job': 'Erik Matti',
    'Tadhana': 'Antoinette Jadaone',
    'BuyBust': 'Erik Matti'
}

# Print the entire dictionary
print("Movie Directors Dictionary: ", movie_directors_dict)

# Access and print the director of the 5th movie.
print()
print("Director of the 5th movie: ", movie_directors_dict['The Hows of Us'])

# Update the director of the 9th movie.
movie_directors_dict['Tadhana'] = 'Cathy Molina'
print()
print("Updated Movie Directors Dictionary: ", movie_directors_dict)

# Delete the 7th movie from the dictionary.
del movie_directors_dict ['Barber Tales']
print()
print("Dictionary after deleting Barber's Tales: ", movie_directors_dict)

# Print the last key-value pair in the dictionary.
last_movie = list(movie_directors_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_movie)
