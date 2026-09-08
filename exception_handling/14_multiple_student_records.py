# 14. Multiple Student Records

# Question : Create a dictionary of students and marks. Ask the user for multiple student names. Handle KeyError without stopping the program.

students_data = {"Alice": 85, "Bob": 90, "John": 75}

def find_mark(student_dict, key):
    try:
        mark = student_dict[key]
    except KeyError:
        print(f"Error: {key} not found.")
    else:
        print(f"{key}'s marks: {mark}")

t = int(input("How many test cases you want : "))

for i in range(t):
    student = input("Enter name: ").capitalize()
    find_mark(students_data, student)