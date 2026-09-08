# 16. Custom Login Exception

# Question: Create a login system. The user gets only 3 attempts. Create a custom exception for invalid login.

user_data = {
    "gemini":"123",
    "chatgpt":"456",
    "claude":"789",
}

class InvalidLoginError(Exception):
    pass

def login(user_name, password):
    clean_name = user_name.lower().strip()
    if clean_name not in user_data or password != user_data[clean_name]:
        raise InvalidLoginError("Invalid username or password")

for i in range(3): 
    user_name = input("Username: ")
    password = input("Password: ")
    try:
        login(user_name, password)
    except InvalidLoginError as e:
        print(f"Error: {e}")
    else:
        print("Login successful")
        break

else:
    print("Account locked")