# city_population_dict.py

#  Dictionary of 10 cities and their corresponding population.
city_population_dict = {   
    'Manila': '27,200,000',
    'Guangzhou': '70,100,00',
    'Tokyo': '41,000,000',
    'Delhi': '34,600,000',
    'Jakarta': '29,200,000',
    'Mumbai': '27,100,000',
    'Seoul': '25,100,000',
    'Cairo': '22,500,000',
    'Dhaka': '22,500,000',
    'Beijing': '21,200,000'
}

# Print the entire dictionary.
print()
print("City Population Dictionary: ", city_population_dict)

# Access and print the population of the 6th city.
print()
print("Population of sixth city 'Mumbai': ", city_population_dict['Mumbai'])

# Update the population of the 3rd city.
city_population_dict['Osaka'] ='17,700,000'
print()
print("Updated City Population Dictionary: ", city_population_dict)

# Delete the 9th city from the dictionary.
del city_population_dict['Dhaka']
print()
print("Dictionary after deleting 'Dhaka': ", city_population_dict)

# Print the last key-value pair in the dictionary.
last_city = list(city_population_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_city)