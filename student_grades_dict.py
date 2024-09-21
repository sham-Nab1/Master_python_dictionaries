# student_grades_dict.py

# Dictionary of 5 students and their corresponding grades.
student_grades_dict = {
    'Student1': 'A+',
    'Student2': 'B+',
    'Student3': 'B',
    'Student4': 'A-',
    'Student5': 'C'
}

# Print the entire dictionary
print("Student Grades Dictionary: ", student_grades_dict)

# Access and print the grade of the 3rd student.
print()
print("Grade of third student: ", student_grades_dict['Student3'])

# Update the grade of the 2nd student.
print()
student_grades_dict['Student2'] = 'A'
print("Updated Student Grades Dictionary: :", student_grades_dict)

# Delete the entry of the 5th student.
del student_grades_dict['Student5']
print()
print("Dictionary after deleting Student5: ", student_grades_dict)

# Print the last key-value pair in the dictionary.
last_student = list(student_grades_dict.items())[-1]
print()
print("Last key-value pair in the dicionary: ", last_student)