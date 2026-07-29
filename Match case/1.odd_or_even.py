# 1. Write a program to check whether a number is 
# *even or odd* using match.

number = int(input("Enter a number : "))

match number :
    case 0 :
        print("Given number is zero")
    case a if a%2 == 0 :
        print(f"{number} is a even number")
    case a if a%2 != 0 :
        print(f"{number} is a odd number")