# 10. Write a program to print the multiplication table of 7.
i = 1
a = int(input("how many rows of 7 tables you want : "))
if 1 <= a <= 100 :
    while i <= a :
        print(f"7 x {i} = {i*7}")
        i += 1