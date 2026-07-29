# 18. Write a Python program to find the second
# largest number in a list using loops.
my_list = [7,3,2,4,6]
if my_list[0] > my_list[1] :
    largest = my_list[0]
    second_largest = my_list[1]
else :
    largest = my_list[1]
    second_largest = my_list[0]
my_list.remove(my_list[0])
my_list.remove(my_list[0])
for i in my_list :
    if i > largest :
        second_largest = largest
        largest = i
    elif i > second_largest :
        second_largest = i
print(f"\nThe second largest number is '{second_largest}'\n")
