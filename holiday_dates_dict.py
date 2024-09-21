# holiday_dates_dict.py

# Dictionary of 10 holidays and their corresponding dates
holiday_dates_dict = {
    'Valentines Day': 'February 14',
    'New Years Eve': 'December 31',
    'Thanksgiving': 'November 24',
    'Independence Day': 'July 4',
    'New Years Day': 'January 1',
    'Labor Day': 'September 5',
    'Christmas': 'December 25',
    'Halloween': 'October 31',
    'Hanukkah': 'December 18',   
    'Easter': 'April 17'  
}

# Print the entire dictionary
print("Holiday Dates Dictionary: ", holiday_dates_dict)

# Access and print the date of the 4th holiday
print()
print("Date of the 4th holiday 'Independence Day': ", holiday_dates_dict['Independence Day'])

# Update the date of the 9th holiday
holiday_dates_dict['Hanukkah'] = 'December 31, 2024'
print()
print("Updated Holiday Dates Dictionary: ", holiday_dates_dict)

# Delete the 2nd holiday from the dictionary
del holiday_dates_dict['New Years Eve']
print()
print("Dictionary after deleting 'New Years Eve': ", holiday_dates_dict)

# Print the last key-value pair in the dictionary
last_holiday = list(holiday_dates_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_holiday)