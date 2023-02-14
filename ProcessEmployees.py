"""
The Customer Service Represetatives (CSRs) in the marketing department with a security clearance of 'TS' were able
to thwart an a,ttack on the server and for that management has decided to reward them with a 10% increase in their salary. 
To evaluate the impact on the budget you have been asked to run a report on the employee file and display the results 
of BEFORE AND AFTER the salary increase. Also calculate the total difference between the old salary and the new
salary (as shown in the image).

You will create a dictionary that has the full employee name as the key and only their NEW salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as shown in the image)
"""

import csv

# open the file
employee_data_file = open("employee_data.csv")

# skip the header
next(employee_data_file)

# create an empty dictionary
employee_dict = {}

# use a loop to iterate through the csv file
for row in employee_data_file:
    data = row.split(",")

    # check if the employee fits the search criteria
    if data[9] == "TS":
        # add to dict
        employee_dict[data[1] + " " + data[2]] = (
            float(data[5]),
            float(data[5]) + (float(data[5]) * 0.1),
        )

print()
print("=========================================")
print()

# iternate through the dictionary and print out the key and value as per image
for name, salary in employee_dict.items():
    print(
        "Employee Name:", name, "Current Salary:", salary[0], "New Salary:", salary[1]
    )

print()
print("=========================================")
print()

# print out the total difference between the old salary and the new salary as per image.
total_dif = 0

for name, salary in employee_dict.items():
    total_dif += salary[1] - salary[0]

print("Total Increase in Salary:", total_dif)
