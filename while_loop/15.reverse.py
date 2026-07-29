# 15. Write a program to reverse a number using a for loop.
a = int(input("Enter your digit : "))
result = 0
while a > 0 :
    b = a % 10
    result = (result*10) +  b
    a = a//10
print(result)
print(type(result))