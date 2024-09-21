# movie_genres_dict.py

# Dictionary of 8 movie genres and their corresponding example movies
movie_genres_dict = {
    'Documentary': 'My Love, Don’t Cross That River',
    'Animation': 'Leafie A Hen Into the Wild',
    'Historical': 'The King’s Affection',
    'Musical': 'The King and the Clown',
    'Comedy': 'My Annoying Brother',
    'Thriller': 'Memories of Murder',
    'Drama': 'Parasite',
    'Action': 'Oldboy', 
}

# Print the entire dictionary
print("Movie Genres Dictionary: ", movie_genres_dict)

# Access and print the example movie of the 3rd genre
print()
print("Example movie of the 3rd genre 'Historical': ", movie_genres_dict['Historical'])

# Update the example movie of the 5th genre
movie_genres_dict['Comedy'] = 'The Way Home'
print()
print("Updated Movie Genres Dictionary: ", movie_genres_dict)

# Delete the 7th genre from the dictionary
del movie_genres_dict['Drama']
print()
print("Dictionary after deleting ''Drama': ", movie_genres_dict)

# Print the last key-value pair in the dictionary
last_genre = list(movie_genres_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_genre)
