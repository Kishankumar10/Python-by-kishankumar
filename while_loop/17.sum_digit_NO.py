# 17. Write a program to find the sum of digits
#  of a number (example: 564 → 15).
a = int(input("Enter a number : "))
total = 0 
while a>0:
    last = a % 10 
    a = a//10
    total += last
print(total)
