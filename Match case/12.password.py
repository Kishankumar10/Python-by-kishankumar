# 12. Write a program to validate a 
#*username and password* using match.

username = input("\n\tusername : ")
password = input("\tpassword : ")

match (username,password) :
    case ("Kishankumar","python@123") :
        print("\n\tpassword matched !\n")
    case _ :
        print("\n\tinvalid username or password\n")
    

