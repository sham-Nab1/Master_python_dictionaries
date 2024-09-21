# city_landmarks_dict.py

# Dictionary of 8 cities and their famous landmarks
city_landmarks_dict = {
    'Rio de Janeiro': 'Christ the Redeemer',
    'Beijing': 'Great Wall of China',
    'Sydney': 'Sydney Opera House',
    'Los Angeles': 'Hollywood Sign',
    'Bangkok': 'Grand Palace',
    'Moscow': 'Red Square',
    'Dubai': 'Burj Khalifa',
    'Rome': 'Colosseum',
   
}

# Print the entire dictionary
print("City Landmarks Dictionary: ", city_landmarks_dict)

# Access and print the landmark of the 6th city
print()
print("Landmark of the 6th city 'Moscow': ", city_landmarks_dict['Moscow'])

# Update the landmark of the 2nd city
city_landmarks_dict['Beijing'] = 'Great Wall of China (Updated)'
print()
print("Updated City Landmarks Dictionary: ", city_landmarks_dict)

# Delete the 7th city from the dictionary
del city_landmarks_dict['Dubai']
print()
print("Dictionary after deleting 'Dubai': ", city_landmarks_dict)

# Print the last key-value pair in the dictionary
last_city = list(city_landmarks_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_city)
