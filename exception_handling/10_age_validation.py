# 10. Age Validation

# Question : Write a function check_age(age) that raises a ValueError if the age is negative.


n = int(input("Enter your age : "))

def check_age(age):
    try :
        if age < 0:
            raise ValueError("Error: Age cannot be negative.")
    except ValueError as e:
        print(e)
    else:
        print(f"Valid age: {age}")

check_age(n)