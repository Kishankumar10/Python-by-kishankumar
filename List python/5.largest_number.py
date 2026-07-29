# 5. Write a Python program to find the 
# largest number in a list using a loop.

my_list = [12,9,23,57,7]
largest_number = my_list[0]
for i in my_list :
    if i > largest_number :
        largest_number = i 
print(f"\nThe largest number in the list is {largest_number}\n")
