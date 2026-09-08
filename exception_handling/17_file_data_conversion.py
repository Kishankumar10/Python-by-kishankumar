# 17. File Data Conversion

# Write a program that reads the file and converts each line to an integer. Handle invalid values without stopping the program.

# version - 1:

with open("demo.txt", "r") as file: 
    data = file.readlines()
    for i in data:
        line = (i.strip("\n"))
        try:
            res = int(line)
        except ValueError:
            print(f"Error: '{line}' is not a valid number.")
        else:
            print(res)

# version - 2:

# actually file is iterable

with open("demo.txt", "r") as file: 
    for i in file:
        line = (i.strip("\n"))
        try:
            res = int(line)
        except ValueError:
            print(f"Error: '{line}' is not a valid number.")
        else:
            print(res)