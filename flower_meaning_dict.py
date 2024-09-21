# flower_meaning_dict.py

# Dictionary of 8 flowers and their symbolic meanings
flower_meanings_dict = {
    'Sunflower': 'Adoration and loyalty',
    'Chrysanthemum': 'Optimism and joy',
    'Marigold': 'Warmth and creativity',
    'Lily': 'Purity and refined beauty',   
    'Daisy': 'Innocence and purity',
    'Rose': 'Love and passion',   
    'Tulip': 'Perfect love',
    'Iris': 'Hope and faith'
}

# Print the entire dictionary
print("Flower Meanings Dictionary: ", flower_meanings_dict)

# Access and print the meaning of the 5th flower
print()
print("Meaning of the 5th flower 'Daisy': ", flower_meanings_dict['Daisy'])

# Update the meaning of the 7th flower
flower_meanings_dict['Tulip'] = 'Exotic beauty and strength'
print()
print("Updated Flower Meanings Dictionary: ", flower_meanings_dict)

# Delete the 6th flower from the dictionary
del flower_meanings_dict['Rose']
print()
print("Dictionary after deleting 'Rose': ", flower_meanings_dict)

# Print the last key-value pair in the dictionary
last_flower = list(flower_meanings_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_flower)