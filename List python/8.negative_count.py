# 8. Write a Python program to count how
# many negative numbers are in a list.

my_list = [6,-9,3,-1,8]
count = 0
for i in my_list :
    if i < 0 : 
        count += 1
print(f"\nThe number of -ve number in the list is {count}\n")