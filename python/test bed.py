##Check the type of triangel

a=int(input("enter the length of first side:"))
b=int(input("enter the length of second side:"))
c=int(input("enter the length of third side:"))


if a==0 or b==0 or c==0:
    print("triangles sides have no zero length")
elif a<0 or b<0 or c<0:
    print("triangles have no negative length values")
elif not(a+b>c and b+c>a and a+c>b):
    print("your values are are not from a triangle")
elif a==b==c:
    print("it is an equilateral triangle")
elif a==b or b==c or c==a:
    print("it is an isosceles triangle")
else:
    print("it is a scalene triangle")
