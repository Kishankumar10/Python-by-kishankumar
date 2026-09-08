# 5. Dictionary Key Handling

# Question : Create a dictionary containing student names and marks. Ask the user for a student's name and display their marks. Handle KeyError.

students = {"Alice": 85, "Bob": 90, "John": 78}

key = input("Enter a student name: ")

try:
    extracted_value = students[key]
except KeyError:
    print("Error: Student not found.")
else :
    print(extracted_value)