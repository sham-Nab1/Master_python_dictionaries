# music_albums_dict.py

# Dictionary of 10 music albums and their release years
music_albums_dict = {
    'Kristel Fulgar - The Next Chapter': 2015,
    'KZ Tandingan - Soul Supremacy': 2020,
    'Samantha Bernardo - The Album': 2021,
    'Yeng Constantino - Araw-Araw': 2022,
    'Moira Dela Torre - Malaya': 2020,
    'Ben&Ben - Limasawa Street': 2019,
    'TJ Monterde - Ikaw at Ako': 2014,  
    'Angeline Quinto - Higher': 2018,   
    'Ebe Dancel - Bawat Daan': 2018,
    'Dionela - Ang Kanta Ko': 2020,
}

# Print the entire dictionary
print("Music Albums Dictionary: ", music_albums_dict)

# Access and print the release year of the 3rd album
print()
print("Release year of the 3rd album ('Samantha Bernardo - The Album'): ", music_albums_dict['Samantha Bernardo - The Album'])

# Update the release year of the 8th album
music_albums_dict['Angeline Quinto - Higher'] = 2021
print()
print("Updated Music Albums Dictionary: ", music_albums_dict)

# Delete the 5th album from the dictionary
del music_albums_dict['Moira Dela Torre - Malaya']
print()
print("Dictionary after deleting 'Moira Dela Torre - Malaya': ", music_albums_dict)

# Print the last key-value pair in the dictionary
last_album = list(music_albums_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_album)