# app_store_ratings_dict.py

# Dictionary of 10 apps and their user ratings
app_store_ratings_dict = {
    'Instagram': 4.8,
    'Pinterest': 4.6,
    'LinkedIn': 4.3,
    'WhatsApp': 4.7,
    'Facebook': 4.2,
    'Snapchat': 4.5,
    'Spotify': 4.5,
    'YouTube': 4.6,
    'Twitter': 4.4,
    'TikTok': 4.9,   
}

# Print the entire dictionary
print("App Store Ratings Dictionary: ", app_store_ratings_dict)

# Access and print the rating of the 6th app
print()
print("Rating of the 6th app 'Facebook': ", app_store_ratings_dict['Facebook'])

# Update the rating of the 8th app
app_store_ratings_dict['YouTube'] = 4.5
print()
print("Updated App Store Ratings Dictionary: ", app_store_ratings_dict)

# Delete the 9th app from the dictionary
del app_store_ratings_dict['Twitter']
print()
print("Dictionary after deleting 'Twitter': ", app_store_ratings_dict)

# Print the last key-value pair in the dictionary
last_app = list(app_store_ratings_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_app)
