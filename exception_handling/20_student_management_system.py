# 20. Student Management System

# Build a menu-driven student management system using exception handling.
# The program should support:
# 	1. Add Student
# 	2. Search Student
# 	3. Update Marks
# 	4. Delete Student
# 	5. Display Students
# 	6. Exit

students = {
    101: {"Name": "Alice", "Marks": 85},
    102: {"Name": "Bob", "Marks": 90}
}

# Exception classes

class DuplicateIDError(Exception):
    pass

class StudentNotFoundError(Exception):
    pass

# Functions

def print_student_info(student_id, name, marks):
    print(f"Student ID: {student_id}")
    print(f"Name: {name}")
    print(f"Marks: {marks}")

def add_student(student_id, name, marks):
    if student_id in students:
        raise DuplicateIDError(f"Student with ID {student_id} already exists.")
    students[student_id] = {"Name": name, "Marks": marks}

def search_student(student_id):
    if student_id not in students:
        raise StudentNotFoundError(f"Student with ID {student_id} not found.")
    print_student_info(student_id, students[student_id]["Name"], students[student_id]["Marks"])

def update_mark(student_id, mark):
    if student_id not in students:
        raise StudentNotFoundError(f"Student with ID {student_id} not found.")
    students[student_id]["Marks"] = mark

def delete_student(student_id):
    if student_id not in students:
        raise StudentNotFoundError(f"Student with ID {student_id} not found.")   
    del students[student_id]

def display_students():
    for student_id, info in students.items():
        print_student_info(student_id, info["Name"], info["Marks"])

while True:
    try:
        print()
        menu = int(input("Enter your menu number: "))
        print()
    except ValueError:
        print("Invalid menu number")
        continue
    match menu:
        case 1:  # Add Student
            try:
                student_id = int(input("Enter student ID: "))
                name = input("Enter name: ")
                mark = int(input("Enter marks: "))
                add_student(student_id, name, mark)
            except ValueError:
                print("Invalid input")
            except DuplicateIDError as e:
                print(f"Error: {e}")
            else:
                print("Student successfully added")
        case 2:  # Search Student
            try:
                student_id = int(input("Enter student ID: "))
                search_student(student_id)
            except ValueError:
                print("Invalid input")
            except StudentNotFoundError as e:
                print(f"Error: {e}")
        case 3:  # Update Marks
            try:
                student_id = int(input("Enter student ID: "))
                mark = int(input("Enter marks: "))
                update_mark(student_id, mark)  
            except ValueError:
                print("Invalid input")
            except StudentNotFoundError as e:
                print(f"Error: {e}")
        case 4:
            try:  # Delete Student
                student_id = int(input("Enter student ID: "))
                delete_student(student_id)
            except ValueError:
                print("Invalid input")
            except StudentNotFoundError as e:
                print(f"Error: {e}")
            else:
                print("Deletion successful")
        case 5:  # Display Students
            display_students()
        case 6:  # Exit
            break
        case _:  # fallback
            print("Invalid menu choice.")