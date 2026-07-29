# 2. Write a program to check whether a number 
# is *positive, negative, or zero using match.

number = int(input("Enter a number : "))
match number :
    case 0 :
        print("Given number is zero")
    case a if a > 0 :
        print(f"{number} is a positive number")
    case a if a < 0 :
        print(f"{number} is a negative number")