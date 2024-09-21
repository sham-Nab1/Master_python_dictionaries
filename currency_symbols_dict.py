# currency_symbols_dict.py

# Dictionary of 10 currencies and their symbols
currency_symbols_dict = {
    'United States Dollar': '$',
    'South African Rand': 'R',
    'Australian Dollar': 'A$',
    'South Korean Won': '₩',
    'British Pound': '£',
    'Swiss Franc': 'CHF',
    'Chinese Yuan': '¥',
    'Indian Rupee': '₹',
    'Japanese Yen': '¥',
    'Euro': '€'  
}

# Print the entire dictionary
print("Currency Symbols Dictionary: ", currency_symbols_dict)

# Access and print the symbol of the 5th currency
print()
print("Symbol of the 5th currency 'British Pound': ", currency_symbols_dict['British Pound'])

# Update the symbol of the 9th currency
currency_symbols_dict['Indian Rupee'] = 'INR'
print()
print("Updated Currency Symbols Dictionary: ", currency_symbols_dict)

# Delete the 3rd currency from the dictionary
del currency_symbols_dict['Australian Dollar']
print()
print("Dictionary after deleting 'Australian Dollar': ", currency_symbols_dict)

# Print the last key-value pair in the dictionary
last_currency = list(currency_symbols_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_currency)