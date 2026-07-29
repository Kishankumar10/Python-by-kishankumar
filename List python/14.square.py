# 14. Write a Python program to create a new list
# containing the squares of each element.

my_list = [1,9,3,6,5]
square_list = []
for i in my_list :
    square_list.append(i**2)
print("\n",square_list,end = "\n\n")