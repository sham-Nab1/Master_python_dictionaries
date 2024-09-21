# element_symbols_dict.py

# Dictionary of 10 elements and their chemical symbols
element_symbols_dict = {
    'Hydrogen': 'H',
    'Helium': 'He',
    'Lithium': 'Li',
    'Beryllium': 'Be',
    'Boron': 'B',
    'Carbon': 'C',
    'Nitrogen': 'N',
    'Oxygen': 'O',
    'Fluorine': 'F',
    'Neon': 'Ne'
}

# Print the entire dictionary
print("Element Symbols Dictionary: ", element_symbols_dict)

# Access and print the symbol of the 6th element
print()
print("Symbol of the 6th element (Carbon): ", element_symbols_dict['Carbon'])

# Update the symbol of the 8th element
element_symbols_dict['Oxygen'] = 'O2'
print()
print("Updated Element Symbols Dictionary: ", element_symbols_dict)

# Delete the 9th element from the dictionary
del element_symbols_dict['Fluorine']
print()
print("Dictionary after deleting 'Fluorine': ", element_symbols_dict)

# Print the last key-value pair in the dictionary
last_element = list(element_symbols_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_element)