# Login logic version-1

db_name = "Kishan"
db_password = "k@12"
name = input("Enter your name : ")
password = input("Enter your password : ")

if name != "":
    if name == db_name :
        if password != "" :
            if password == db_password :
                print("Login successful")
            else :
                print("Incorrect password")
        else :
            print("Password is empty")
    else :
        print("Incorrect name")
else : 
    if password != "" :
        print("Name is empty")
    else :
        print("Both name and password are empty")
    