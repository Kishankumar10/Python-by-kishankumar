# 9. Write a program to check whether a 
# given year is a *leap year* using match.
year = int(input("Enter a year : "))
match year :
    case a if ((a%4==0 and a%100!=0) or a%400==0 ) :
        print(f"{year} is a leap year")
    case _ :
        print(f"{year} is not a leap year")
