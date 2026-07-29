## Check Leap Year

##The 3 Rules for Leap Years
##The 4-Year Rule: If a year is evenly divisible by 4, it is generally a leap year (e.g., 2024)
##The 100-Year Exception: If a year is also evenly divisible by 100, it is not a leap year (e.g., 1900)
##The 400-Year Override: If that century year is evenly divisible by 400, it is a leap year (e.g., 2000)

a=int(input("enter the year:"))

if (a%4==0 and a%100!=0) or a%400==0 :
    print("the entered year is a leap year")
else:
    print("the entered year is not a leap year")
