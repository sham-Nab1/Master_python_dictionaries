# phone_models_dict.py

# Dictionary of 10 phone models and their manufacturers
phone_models_dict = {
    'Realme GT 2 Pro': 'Realme',    
    'Asus Zenfone 9': 'Asus',
    'Galaxy S23': 'Samsung',
    'Oppo Find X5': 'Oppo',
    'Huawei P50': 'Huawei',
    'Xiaomi 12': 'Xiaomi',
    'iPhone 14': 'Apple',
    'Nokia G20': 'Nokia',  
    'Pixel 7': 'Google',
    'Vivo X80': 'Vivo'
}

# Print the entire dictionary
print("Phone Models Dictionary: ", phone_models_dict)

# Access and print the manufacturer of the 2nd phone model
print()
print("Manufacturer of the 2nd phone model 'Asus Zenfone 9': ", phone_models_dict['Asus Zenfone 9'])

# Update the manufacturer of the 8th phone model
phone_models_dict['Oppo Find X5'] = 'Oppo (Updated)'
print()
print("Updated Phone Models Dictionary: ", phone_models_dict)

# Delete the 6th phone model from the dictionary
del phone_models_dict['Xiaomi 12']
print()
print("Dictionary after deleting 'Xiaomi 12': ", phone_models_dict)

# Print the last key-value pair in the dictionary
last_phone = list(phone_models_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_phone)