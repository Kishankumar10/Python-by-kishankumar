# 14. Write a program to count the digits of a number (example: 54321).
a = int(input("Enter your digit : "))
d = 0
while a > 0 :
    a = a//10
    d += 1
print(d)