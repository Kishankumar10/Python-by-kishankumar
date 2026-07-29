##14. Write a program to count the digits
##of a number (example: 54321).

a = input("enter the numbers to count the numbers:")
    #string only works and int shows error

count = 0

for i in a:
    count += 1

print(f"the number {a} has a {count} digits")
