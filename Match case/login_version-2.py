# Login logic version-2

db_name = "Kishankumar"
db_password = "k@12"

while True :
    name = input("Username : ")
    if name != "":
        if name == db_name :
            password = input("Password : ")
            if password != "" :
                if password == db_password :
                    break
                else :
                    print("Incorrect password\n")
            else :
                print("Password is empty\n")
        else :
            print("Incorrect name\n")
    else : 
            print("Name is empty\n")

print("Login successful")
















