"""
This script will generate output.json with the help data.json and reference excel sheet
provided along with BMI value
"""

import json

with open("data.json", "r") as read_file:
    data = json.load(read_file)
    read_file.close()

output = {}

for key in data.keys():
    bmi = data[key]['WeightKg']/(data[key]['HeightCm']/100)
    if bmi <= 18.4:
        output[key] = {'BMI': round(bmi, 2), 'BMI_Range': 'Underweight', 'Health risk': 'Malnutrition risk'}
    if 18.5 <= bmi <= 24.9:
        output[key] = {'BMI': round(bmi, 2), 'BMI_Range': 'Normal weight', 'Health risk': 'Low risk'}
    if 25 <= bmi <= 29.9:
        output[key] = {'BMI': round(bmi, 2), 'BMI_Range': 'Overweight', 'Health risk': 'Enhanced risk'}
    if 30 <= bmi <= 34.9:
        output[key] = {'BMI': round(bmi, 2), 'BMI_Range': 'Moderately obese', 'Health risk': 'Medium risk'}
    if 35 <= bmi <= 39.9:
        output[key] = {'BMI': round(bmi, 2), 'BMI_Range': 'Severely obese', 'Health risk': 'High risk'}
    if bmi >= 40:
        output[key] = {'BMI': round(bmi, 2), 'BMI_Range': 'Very severely obese', 'Health risk': 'Very High risk'}

with open('output.json', 'w') as write_file:
    json.dump(output, write_file, indent="")
    write_file.close()
