# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   Harpreet Bassi, 7/29/2024,Created Script for Assignment05
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: list = []  # one row of student data
students: list = []  # a table of student data
json_data: str = ''  # Holds combined string data.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

import json

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    with open(FILE_NAME, "r") as file:
        students = json.load(file)
        for item in students:
            print (f"First Name: {item['first_name']}, Last Name: {item['last_name']}, Course: {item['course_name']}")
# Include the except statements to show if the following do not happen, state the print() statement assigned
except FileNotFoundError:
        print(f"File {FILE_NAME} not found. Starting with an empty list.")
except json.JSONDecodeError:
        print(f"Error reading {FILE_NAME}. Starting with an empty list.")
except Exception as e:
        print(f"Unexpected error reading {FILE_NAME}: {e}")

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("First name must contain only alphabetical characters.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("Last name must contain only alphabetical characters.")
            course_name = input("Please enter the name of the course: ")

            student_data = {'first_name': student_first_name, 'last_name': student_last_name, 'course_name': course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
            continue
        except ValueError as e:
            print(e)

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-" * 50)  #display the 50 hyphens
        for student in students:
            print(f"Student {student['first_name']} {student['last_name']} is enrolled in {student['course_name']}")
        print("-" * 50)  #display the 50 hyphens
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            with open(FILE_NAME, "w") as file:
                json.dump(students, file, indent=1) #Used Indent=1 for better printing

            print("The following data was saved to file!")

        except Exception as e:
            print('Unexpected error saving the data to the file')
            print(e)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
