# 3. Multiple Exceptions

# Question : Write a program that accepts two numbers and performs division. Handle both ValueError and ZeroDivisionError

try:
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    res = a / b
except ValueError:
    print("Error: Invalid input.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print(res)