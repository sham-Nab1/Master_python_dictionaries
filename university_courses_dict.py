# university_courses_dict.py

# Dictionary of 8 universities in the Philippines and their popular courses
university_courses_dict = {
    'University of the Philippines': 'Bachelor of Arts in Communication',
    'Ateneo de Manila University': 'Bachelor of Science in Management',
    'De La Salle University': 'Bachelor of Science in Accountancy',
    'University of Santo Tomas': 'Bachelor of Fine Arts',
    'Mapúa University': 'Bachelor of Science in Engineering',
    'San Beda University': 'Bachelor of Laws',
    'University of San Carlos': 'Bachelor of Science in Information Technology',
    'Adamson University': 'Bachelor of Science in Business Administration'
}

# Print the entire dictionary
print("University Courses Dictionary: ", university_courses_dict)

# Access and print the course of the 3rd university
print()
print("Course of the 3rd university (De La Salle University): ", university_courses_dict['De La Salle University'])

# Update the course of the 5th university
university_courses_dict['Mapúa University'] = 'Bachelor of Science in Architecture'
print()
print("Updated University Courses Dictionary: ", university_courses_dict)

# Delete the 7th university from the dictionary
del university_courses_dict['University of San Carlos']
print()
print("Dictionary after deleting 'University of San Carlos': ", university_courses_dict)

# Print the last key-value pair in the dictionary
last_university = list(university_courses_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_university)