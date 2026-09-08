# 11. Marks Validation

# Question : Write a program that accepts marks. Raise an exception if marks are less than 0 or greater than 100.

n = int(input("Enter marks: "))

def check_mark(mark):
    try:
        if not 0 <= mark <= 100:
            raise ValueError("Invalid input")
    except ValueError:
        print("Error: Marks must be between 0 and 100.")
    else:
        print(f"Marks accepted: {mark}")

check_mark(n)