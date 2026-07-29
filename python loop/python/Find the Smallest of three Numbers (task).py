##Find the Smallest of three Numbers

a=int(input("enter your first number :"))
b=int(input("enter your second number :"))
c=int(input("enter your third number :"))

if a==b or b==c or a==c :
    print("don't enter same number again and again")
elif a<b and a<c :
    print("first number is the smallest number")
elif b<a and b<c :
    print("second number is the smallest number")
else  :
    print("third number is the smallest number")

