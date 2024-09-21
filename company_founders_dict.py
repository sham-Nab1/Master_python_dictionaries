# company_founders_dict.py

# Dictionary of 8 companies and their founders
company_founders_dict = {
    'Meralco (Manila Electric Company)': 'Francisco C. Dizon',
    'Robinsons Retail Holdings': 'John Gokongwei Jr.',
    'Jollibee Foods Corporation': 'Tony Tan Caktiong',
    'Petron Corporation': 'Robert M. L. De La Torre',
    'San Miguel Corporation': 'Andres Soriano',
    'Philippine Airlines': 'Andres Soriano',
    'Cebu Pacific Air': 'Lance Gokongwei',   
    'Globe Telecom': 'Isabelita Dy'   
}

# Print the entire dictionary
print("Company Founders Dictionary: ", company_founders_dict)

# Access and print the founder of the 6th company
print()
print("Founder of the 6th company 'Philippine Airlines': ", company_founders_dict['Philippine Airlines'])

# Update the founder of the 2nd company
company_founders_dict['Robinsons Retail Holdings'] = 'Hans Sy'
print()
print("Updated Company Founders Dictionary: ", company_founders_dict)

# Delete the 8th company from the dictionary
del company_founders_dict['Globe Telecom']
print()
print("Dictionary after deleting 'Globe Telecom': ", company_founders_dict)

# Print the last key-value pair in the dictionary
last_company = list(company_founders_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_company)