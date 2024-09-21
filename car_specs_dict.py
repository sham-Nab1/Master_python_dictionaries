 # car_specs_dict.py

 # Dictionary of 10 car models and their engine specifications
car_specs_dict = {
    'Mercedes-Benz C-Class': '2.0L Turbo I4, 255 hp',
    'Hyundai Sonata': '2.5L 4-cylinder, 191 hp',
    'Chevrolet Malibu': '1.5L Turbo I4, 160 hp',
    'Nissan Altima': '2.5L 4-cylinder, 188 hp',
    'Ford Mustang': '2.3L EcoBoost I4, 310 hp',
    'Toyota Camry': '2.5L 4-cylinder, 203 hp',
    'Honda Accord': '1.5L Turbo I4, 192 hp',
    'BMW 3 Series': '2.0L Turbo I4, 255 hp',
    'Porsche 911': '3.0L Turbo H6, 379 hp',
    'Lexus ES': '2.5L 4-cylinder, 203 hp'  
}

# Print the entire dictionary
print("Car Specs Dictionary: ", car_specs_dict)

# Access and print the specifications of the 4th car model
print()
print("Specifications of the 4th car model 'Nissan Altima': ", car_specs_dict['Nissan Altima'])

# Update the specifications of the 9th car model
car_specs_dict['Porsche 911'] = '2.5L 4-cylinder, 250 hp'
print()
print("Updated Car Specs Dictionary: ", car_specs_dict)

# Delete the 5th car model from the dictionary
del car_specs_dict['Ford Mustang']
print()
print("Dictionary after deleting 'Ford Mustang': ", car_specs_dict)

# Print the last key-value pair in the dictionary
last_car = list(car_specs_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_car)