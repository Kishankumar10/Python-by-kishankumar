# 18. Nested Exception Handling

# Write a program that:
# 	1. Takes two numbers.
# 	2. Divides them.
# 	3. Stores the result in a list.
# 	4. Asks the user for an index.
# Handles ValueError, ZeroDivisionError, and IndexError.

my_list = []
t = int(input("Enter number of test cases: "))

for i in range(t):
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
    except ValueError:
        print("Error: Please enter a valid integer.")
    else:
        try:
            div = a / b
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        else:
            my_list.append(div)

try:
    n = int(input("Enter a index position: "))
except ValueError:
    print("Error: Index must be a integer")
else:
    try:
        res = my_list[n]
    except IndexError:
        print("Error: Index out of range")
    else:
        print(res)