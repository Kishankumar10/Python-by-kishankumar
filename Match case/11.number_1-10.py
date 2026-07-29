# 11. Write a program to check whether a number 
# lies *between 1 and 10* using match.
a = int(input("Enter a number between 1 to 10 : "))
match a :
    case _ if  1 <= a <= 10 :
        print("in range")
    case _ :
        print("out of range")
