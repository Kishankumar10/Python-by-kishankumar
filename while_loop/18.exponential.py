# 18. Write a program to calculate power of a 
# number using loops (example: 2⁵).
base = int(input("Enter your base : "))
power = int(input("Enter your power : "))
result = 1
while power > 0 :
    result *= base
    power -= 1
print(result)