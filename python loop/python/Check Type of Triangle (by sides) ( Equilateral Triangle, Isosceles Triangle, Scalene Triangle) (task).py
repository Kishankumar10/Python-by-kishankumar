## Check Type of Triangle (by sides)
##( Equilateral Triangle, Isosceles Triangle, Scalene Triangle)

a=int(input("length of first side of triangle:"))
b=int(input("length of second side of triangle:"))
c=int(input("length of third side of triangle:"))

if a==b and b==c and c==a:
    print("it is a equilateral triangle")
elif a==b or b==c or c==a:
    print("it is a Isosceles Triangle ")
else:
    print("it is a Scalene Triangle")
