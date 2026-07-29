# Login logic version-5 (readable i think)

db_name = "Boss"          # stored username 
db_password = "k@12"      # stored password 
attempt = 5               # number of attempts allowed to enter the password

while True :   #unlimited chance is given to enter username

    name = input("Username : ")  # ask for username 
    if name != "":               # check whether username is not empty
        if name == db_name :     # check if the username is correct 
            break
        else :
            print("Incorrect name\n")  # inform user as the username is incorrect
    else : 
        print("Name is empty\n")   # inform user as the username is empty

for current_attempt in range(1,attempt+1) :       
    
    remaining_attempt = (attempt + 1) - current_attempt    # actual attempt left or descending count
    
    if 1 < remaining_attempt <= 3 :
        print(f"You have {remaining_attempt} attempts")   # warns how many attempts left 

    if remaining_attempt == 1 :
        print(f"You have only {remaining_attempt} attempt") # extra condition for grammatical correction

    password = input("Password : ")         # ask for password

    if password != "":                      # check whether password is not empty
        if password == db_password :        # check if the password is correct
            print("Login successful")       # prints the login is successful if password matches
            break                           # stop the loop 
        else :
            print("Incorrect password\n")   # inform user as the password is incorrect
    else : 
        print("password is empty\n")        # inform user as the password is empty

    if remaining_attempt == 1 :
        print("Your account is temporarily locked\n")  # inform user as you account was temporarily is locked
    
    