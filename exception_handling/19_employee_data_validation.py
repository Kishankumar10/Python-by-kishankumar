# 19. Employee Data Validation

# Create a custom exception InvalidEmployeeDataError. Validate the employee's age and salary.

class InvalidEmployeeDataError(Exception):
    pass

employee = {
    "name": "Alice",
    "age": "hj",
    "salary": "gh"
}

def validate(data):
    error = []
    try:
        age = int(data["age"])  
    except ValueError:
        error.append("Error: Invalid age. Age must be an integer.")
    try:
        salary = int(data["salary"])  
    except ValueError:
        error.append("Error: Invalid salary. Salary must be an integer.")
    if error:
        raise InvalidEmployeeDataError("\n".join(error))
    return age,salary

try:
    n = validate(employee)
except InvalidEmployeeDataError as e:
    print(e)
else:
    print("Employee data is valid.")
    print(f"Name: {employee['name']}")
    print(f"Age: {n[0]}")
    print(f"Salary: {n[1]}")