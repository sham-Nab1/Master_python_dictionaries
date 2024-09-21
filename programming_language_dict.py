# programming_language_dict.py

# Dictionary of 7 programming languages and their developers.
programming_languages_dict = {
    'Go': 'Robert Griesemer, Rob Pike, Ken Thompson',
    'C++': 'Bjarne Stroustrup',
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'JavaScript': 'Brendan Eich',
    'Swift': 'Chris Lattner',
    'Java': 'James Gosling'  
}

# Print the entire dictionary
print("Programming Languages Dictionary: ", programming_languages_dict)

# Access and print the developer of the 4th programming language.
print()
print("Developer of the 4th programming language: ", programming_languages_dict['JavaScript'])

# Update the developer of the 6th programming language.
programming_languages_dict['Swift'] = 'Apple Inc.'
print()
print("Updated Programming Languages Dictionary: ", programming_languages_dict)

# Delete the 2nd programming language from the dictionary.
del programming_languages_dict['Java']
print()
print("Dictionary after deleting Java: ", programming_languages_dict)

# Print the last key-value pair in the dictionary.
last_language = list(programming_languages_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_language)
