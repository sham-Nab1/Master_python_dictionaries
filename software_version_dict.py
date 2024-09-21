# software_version_dict.py

# Dictionary of 6 software programs and their latest versions
software_versions_dict = {
    'Microsoft Office': '2023',
    'Adobe Photoshop': '2024',
    'Google Chrome': '117.0.5938.92',
    'Mozilla Firefox': '118.0',
    'Slack': '4.28.0',
    'Zoom': '5.14.0'
}

# Print the entire dictionary
print("Software Versions Dictionary: ", software_versions_dict)

# Access and print the version of the 4th software
print()
print("Version of the 4th software (Mozilla Firefox): ", software_versions_dict['Mozilla Firefox'])

# Update the version of the 2nd software
software_versions_dict['Adobe Photoshop'] = '2024.1'
print()
print("Updated Software Versions Dictionary: ", software_versions_dict)

# Delete the 5th software from the dictionary
del software_versions_dict['Slack']
print()
print("Dictionary after deleting 'Slack': ", software_versions_dict)

# Print the last key-value pair in the dictionary
last_software = list(software_versions_dict.items())[-1]
print()
print("Last key-value pair in the dictionary: ", last_software)