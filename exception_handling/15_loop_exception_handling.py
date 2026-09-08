# 15. Exception Handling in a Loop

# Question: Write a program that repeatedly accepts integers. If the user enters an invalid value, display an error and continue. Stop when the user enters 0.

while True:
    try:
        num = int(input("Enter a integer: "))
    except ValueError:
        print("Error: Invalid input.")
    else:
        if num == 0:
            print("Program stopped.")
            break
        print(f"{num} accepted.")