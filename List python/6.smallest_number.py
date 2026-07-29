# 6. Write a Python program to find the 
# smallest number in a list using a loop.

my_list = [12,9,23,57,7]
smallest_number = my_list[0]
for i in my_list :
    if i < smallest_number :
        smallest_number = i 
print(f"\nThe smallest number in the list is {smallest_number}\n")