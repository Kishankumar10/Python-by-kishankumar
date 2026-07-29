##18. Write a program to calculate power
##of a number using loops (example: 2⁵).

base = int(input("enter your base:"))
power = int(input("enter your power:"))

result = 1
for i in range(1,power+1):
    result *= base
    
print(result)
    
    
