# 5. Variable Swapping (The In-Place Method)

# Practice Problem: Write a program to swap the values of two variables, a and b, without using a third temporary variable.

a = 5
b = 10

a, b = b, a
print(a, b)