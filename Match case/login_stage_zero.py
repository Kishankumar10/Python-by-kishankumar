db_name = "Kishankumar"
db_password = "k0710"
name = input("Enter your name :")
password = input("Enter your password :")
if name != "" and password != "" :
    if name != db_name and password != db_password :
        print("both password and name are incorrect")
    elif name != db_name :
        print("incorrect name")
    elif password != db_password :
        print("incorrect password")
    else :
        print("Login successfull")
else :
    if name == "" and password == "" :
        print("both password and name are empty")
    elif password == "" :
        print(" password is empty ")
    else :
        print(" name are empty")