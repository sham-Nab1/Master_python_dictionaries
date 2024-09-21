# artist_songs_dict.py

# Dictionary of 8 artists and their top songs in the Philippines
artist_songs_dict = {
    'KZ Tandingan': 'Mahal na Mahal',
    'Moira Dela Torre': 'Tagpuan',
    'Yeng Constantino': 'Ikaw',   
    'Polo Ravales': 'Sa Kanya',
    'Sarah Geronimo': 'Tala',
    'Bamboo': 'Hallelujah',   
    'Ben&Ben': 'Leaves',  
    'Gloc-9': 'Upuan' 
}

# Print the entire dictionary
print("Artist Songs Dictionary: ", artist_songs_dict)

# Access and print the top song of the 3rd artist
print()
print("Top song of the 3rd artist 'Yeng Constantino': ", artist_songs_dict['Yeng Constantino'])

# Update the top song of the 6th artist
artist_songs_dict['Bamboo'] = 'Kapit'
print()
print("Updated Artist Songs Dictionary: ", artist_songs_dict)

# Delete the 7th artist from the dictionary
del artist_songs_dict['Ben&Ben']
print()
print("Dictionary after deleting 'Ben&Ben': ", artist_songs_dict)

# Print the last key-value pair in the dictionary
last_artist = list(artist_songs_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_artist)