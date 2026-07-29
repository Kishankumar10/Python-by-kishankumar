# 13. Write a program to identify a *shape name* 
# based on the number of sides using match.
sides = abs(int(input("Enter the number of sides of a polygon : ")))
match sides :
    case _ if sides < 3 :
        print("Atleast three sides are needed for a shape")
    case 3 :
        print("It is a triangle")
    case 4 :
        print("It is a Quadrilateral")
    case 5 :
        print("It is a Pentagon")
    case 6 :
        print("It is a Hexagon")
    case 7 :
        print("It is a Heptagon")
    case 8 :
        print("It is an Octagon")
    case 9 :
        print("It is a Nonagon")
    case 10 :
        print("It is a Decagon")
    case _ if sides > 10 :
       print("It is a polygon with sides greater than 10")
    

