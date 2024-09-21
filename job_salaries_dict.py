# job_salaries_dict.py

# Dictionary of 10 jobs and their average salaries
job_salaries_dict = {
    'Sales Representative': 450000,
    'Marketing Manager': 900000,
    'Software Engineer': 600000,
    'Graphic Designer': 350000,
    'Project Manager': 750000,
    'Civil Engineer': 700000,
    'Data Scientist': 800000,
    'Accountant': 500000,
    'Teacher': 300000,
    'Nurse': 400000
}

# Print the entire dictionary
print("Job Salaries Dictionary: ", job_salaries_dict)

# Access and print the salary of the 3rd job
print()
print("Salary of the 3rd job 'Software Engineer': ", job_salaries_dict['Software Engineer'])

# Update the salary of the 7th job
job_salaries_dict['Data Scientist'] = 850000
print()
print("Updated Job Salaries Dictionary: ", job_salaries_dict)

# Delete the 9th job from the dictionary
del job_salaries_dict['Teacher']
print()
print("Dictionary after deleting 'Teacher': ", job_salaries_dict)

# Print the last key-value pair in the dictionary
last_job = list(job_salaries_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_job)
