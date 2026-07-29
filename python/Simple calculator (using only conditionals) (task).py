##Simple calculator (using +,-,*,/)

a = int(input("enter first number:"))
Arithmetic_operator = (input("enter arithmetic operator:"))
b = int(input("enter second number:"))
                       

if Arithmetic_operator=="+" :
    print(a+b)
elif Arithmetic_operator=="-" :
    print(a-b)
elif Arithmetic_operator=="*" :
    print(a*b)
elif Arithmetic_operator=="/" and b!=0:
    print(a/b)
else :
    print("mathematically impossible")



