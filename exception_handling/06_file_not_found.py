# 06.File Not Found

# Question : Write a program that asks the user for a filename and opens the file. Handle FileNotFoundError.

file_name = input("Enter the file name with extension : ")

try:
    with open(file_name, "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: File not found.")