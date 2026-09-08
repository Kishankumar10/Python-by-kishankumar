# 9. Safe Calculator

# Question : Create a calculator that accepts two numbers and an operator (+, -, *, /). Handle invalid input and division by zero.

try:
    a = float(input("Enter first number: "))
    operator = input("Enter operator: ")
    b = float(input("Enter second number: "))
    if operator not in {"+", "-", "*", "/"}:
        raise ValueError("Invalid operator.")
    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    else:
        result = a / b
except ValueError:
    print("Error: Invalid input.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print(result)