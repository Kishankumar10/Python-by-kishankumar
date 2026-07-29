# 14. Write a program to check whether a number is
# *divisible by both 3 and 5* using match.
number = int(input("Enter a number : "))
match number :
    case _ if number%3 == 0 and number%5 == 0 :
        print(f"{number} is divisible by both 3 and 5")
    case _ :
        print(f"{number} is not divisible by both 3 and 5")
