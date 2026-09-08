# 8. Using else

# Question : Write a program that accepts an integer and prints its square. Use try, except, and else.

try:
    n = int(input("Enter a number : "))
except ValueError:
    print("Error: Please enter an integer.")
else:
    print(f"Square: {n * n}")