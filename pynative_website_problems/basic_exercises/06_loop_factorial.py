# 6. Calculating Factorial with a Loop

# Practice Problem: Write a program that calculates the factorial of a given number (e.g., 5!) using a for loop.

def factorial(num):
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

print(factorial(5))