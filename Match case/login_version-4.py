# Login logic version-4 (not readable)

db_name = "Kishankumar"
db_password = "k@12"

while True :
    name = input("Username : ")
    if name != "":
        if name == db_name :
            break
        else :
            print("Incorrect name\n")
    else : 
            print("Name is empty\n")
for i in range(4,-1,-1) :
    password = input("Password : ")
    if password != "":
        if password == db_password :
            print("\nLogin successful\n")
            break
        else :
            print("Incorrect password\n")
    else : 
            print("password is empty\n")
    if i <= 3 and i > 0 :
        print(f"You have only {i} attempts")
    elif i == 0 :
        print("You account is temporarily locked\n")

    
    