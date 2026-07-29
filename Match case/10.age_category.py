# 10. Write a program to categorize a person based on 
# *age group* (Child, Teen, Adult, Senior) using match.
age=int(input("what is your age : "))
match age :
    case a if a < 0 :
        print("age cannot be negative")
    case a if a < 13 :
        print("you are a child")
    case a if a < 20 :
        print("you are a teenager")
    case a if a < 60 :
        print("you are an adult")
    case _ :
        print("you are a senior citizen")

