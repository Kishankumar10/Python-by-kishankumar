# 4. Write a program to check whether a given
#  day is a *weekday or weekend* using match.\
day = input("Enter the name of the day : ").strip().lower()
match day :
    case "monday"|"tuesday"|"wednesday"|"thursday"|"friday" :
        print("weekday")
    case "sunday"|"saturday" :
        print("weekend")
    case _ :
        print("Invalid day name")