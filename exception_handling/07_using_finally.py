# 7. Using finally

# Question : Write a program that divides two numbers and uses a finally block to display a message regardless of whether an exception occurs.

try:
    a = int(input("Enter your first number : "))
    b = int(input("Enter your second number : "))
    result = a / b
except ValueError:
    print("Error: Please enter a valid integer.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print(result)
finally:
    print("Program execution completed.")