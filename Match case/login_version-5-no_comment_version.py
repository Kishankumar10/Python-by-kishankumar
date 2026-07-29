# Login logic version-5 
db_name = "Kishankumar"    
db_password = "k@12"      
attempt = 5                      

while True :   
    name = input("Username : ")  
    if name != "":               
        if name == db_name :     
            break
        else :
            print("Incorrect name\n")  
    else : 
        print("Name is empty\n")   
for current_attempt in range(1,attempt+1) :       
    
    remaining_attempt = (attempt + 1) - current_attempt    
    if 1 < remaining_attempt <= 3 :
        print(f"You have {remaining_attempt} attempts")   

    if remaining_attempt == 1 :
        print(f"You have only {remaining_attempt} attempt") 

    password = input("Password : ")         
    if password != "":                      
        if password == db_password :        
            print("\nLogin successful\n")       
            break                           
        else :
            print("Incorrect password\n")   
    else : 
        print("password is empty\n")        

    if remaining_attempt == 1 :
        print("Your account is temporarily locked\n")  






