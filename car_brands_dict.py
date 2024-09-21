# car_brands_dict.py

# Dictionary of 10 car brands and their country of origin.
car_brands_dict = {
    'Mercedes-Benz' : 'Germany',
    'Land Rover' : ' UK',
    'Hyundai' : 'South Korea',
    'Toyota' :  'Japan',
    'Ferrari ' : 'Italy',
    'Renault' : 'France',
    'Nissan' : 'Japan',
    'Subaru' : 'Japan',
    'Audi' : 'Germany',
    'Kia' : 'South Korea'
}

# Print the entire dictionary.
print("Car Brands and their Country of Origin Dictionary: ", car_brands_dict)

# Access and print the country of origin of the 3rd car brand.
print()
print("Country of origin of the 3rd car brand: ", car_brands_dict['Hyundai'])

# Update the country of origin of the 7th car brand.
car_brands_dict['Nissan'] = 'UK'
print("Updated Car Brands Dictionary: ", car_brands_dict)

# Delete the 8th car brand from the dictionary.
del car_brands_dict['Subaru']
print()
print("Dictionary after deleting 'Subaru': ", car_brands_dict)

# Print the last key-value pair in the dictionary.
last_brand = list(car_brands_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_brand)

