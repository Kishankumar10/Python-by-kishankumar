# 2. Invalid Integer Input

# Write a program that accepts an integer from the user. If the user enters a non-integer value, handle the ValueError.

try:
    a = int(input("Enter a integer : "))
except ValueError:
    print("Error: Please enter a valid integer.")