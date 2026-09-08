# 1. Division by Zero

# Question: Write a Python program that takes two integers and divides the first number by the second. Handle ZeroDivisionError.

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

try:
    res = a / b
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")