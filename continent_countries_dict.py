 # continent_countries_dict.py

 # Dictionary of 6 continents and a list of 3 countries for each
continent_countries_dict = {
    'Europe': ['Germany', 'France', 'Italy'],
    'Asia': ['China', 'India', 'Japan'],    
    'North America': ['USA', 'Canada', 'Mexico'],
    'South America': ['Brazil', 'Argentina', 'Chile'],
    'Africa': ['Nigeria', 'Kenya', 'South Africa'],
    'Australia': ['Australia', 'New Zealand', 'Papua New Guinea']
}

# Print the entire dictionary
print("Continent Countries Dictionary: ", continent_countries_dict)

# Access and print the countries of the 4th continent
print()
print("Countries of the 4th continent (South America): ", continent_countries_dict['South America'])

# Update the countries of the 5th continent
continent_countries_dict['Europe'] = ['UK', 'Spain', 'Netherlands']
print()
print("Updated Continent Countries Dictionary: ", continent_countries_dict)

# Delete the 6th continent from the dictionary
del continent_countries_dict['Australia']
print()
print("Dictionary after deleting 'Australia': ", continent_countries_dict)

# Print the last key-value pair in the dictionary
last_continent = list(continent_countries_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_continent)