# author_books_dict.py

# Dictionary of 8 authors and their famous books
author_books_dict = {
    'José Rizal': 'Noli Me Tangere',
    'Nick Joaquin': 'The Woman Who Had Two Navels',
    'Carlos Bulosan': 'America Is in the Heart',
    'Lualhati Bautista': 'Bata, Bata... Paano Ka Ginawa?',
    'F. Sionil José': 'The Rosales Saga',
    'Marivi Soliven': 'The Mango Bride',
    'Jessica Zafra': 'The Stories of a Writer',
    'Bobby Yan': 'Bilog na Magsasaka'
}

# Print the entire dictionary
print("Authors and Their Famous Books Dictionary: ", author_books_dict)

# Access and print the book of the 5th author
print()
print("Book of the 5th author (F. Sionil José): ", author_books_dict['F. Sionil José'])

# Update the book of the 7th author
author_books_dict['Jessica Zafra'] = 'Twisted'
print()
print("Updated Authors and Their Books Dictionary: ", author_books_dict)

# Delete the 6th author from the dictionary
del author_books_dict['Marivi Soliven']
print()
print("Dictionary after deleting 'Marivi Soliven': ", author_books_dict)

# Print the last key-value pair in the dictionary
last_author = list(author_books_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_author)
