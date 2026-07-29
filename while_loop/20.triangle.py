# 20. Write a program to print a right-triangle star pattern using a while loop.
a = int(input("how many rows did you want : "))
result = ""
i = 1
while i <= a :
    result += "* "
    i += 1
    print(result)