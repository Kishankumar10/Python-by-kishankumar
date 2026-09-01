# 13. Dictionary Sorting (Lambda)

# Practice Problem: Given a list of dictionaries (representing employees), sort them based on their “salary” in descending order using a lambda function.

employees = [
    {"name": "A", "salary": 50}, 
    {"name": "B", "salary": 70},
    {"name": "C", "salary": 60}
    ]

def sort_employees_by_salary(dictt_data):
    return sorted(dictt_data, key=lambda x : x["salary"], reverse=True)

print(sort_employees_by_salary(employees))