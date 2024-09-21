# book_authors_dict.py

# Dictionary of 12 books and their authors.
book_authors_dict = {
    'Florante at Laura' : 'Francisco Balagtas',
    'Noli Me Tangere' : 'José Rizal',
    'Banaag at Sikat' : 'Lope K. Santos',
    'Lope K. Santos' : 'Jessica Hagedorn',
    'Ang Pahimakas' : 'Edgardo M. Reyes',
    'May Day Eve' : 'Nick Joaquin',
    'Mga Ibong Mandaragit' : 'Amado Hernandez',
    'Smaller and Smaller Circles' : 'F.H. Batacan',
    'Dogeaters' : 'Jessica Hagedorn',
    'Ang Pahimakas' : 'Edgardo M. Reyes',
    'Blue Jeans' : 'Marvin E. A. Araneta',
    'Gabi ng Lagim' : 'Ricky Lee',
}

# Print the entire dictionary.
print("Book Authors Dictionary: ", book_authors_dict)

# Access and print the author of the 9th book.
print()
print("Author of the 9th book: ", book_authors_dict['Dogeaters'])

# Update the author of the 5th book.
book_authors_dict['Ang Pahimakas'] = 'Miguel Syjuco'
print()
print("Updated Book Authors Dictionary: ", book_authors_dict)

# Delete the 3rd book from the dictionary.
del book_authors_dict['Banaag at Sikat']
print()
print("Dictionary after deleting The 'Banaag at Sikat' : ", book_authors_dict)

# Print the last key-value pair in the dictionary.
last_book = list(book_authors_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_book)