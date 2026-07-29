# 15. Write a program to classify a number as *Positive Even, 
# Positive Odd, Zero, or Negative* using match.
number = int(input("Enter a number : "))
match number :
    case 0 :
        print("Zero")
    case _ if number < 0:
        print(f"{number} is a negative number")
    case _ if number % 2 == 0:
        print(f"{number} is a positive even number")
    case _ :
        print(f"{number} is a positive odd number")