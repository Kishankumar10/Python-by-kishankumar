# 19. Write a Python program to check whether 
# a list is sorted in ascending order.

my_list = [5,2,3,4,2,6]
ascending = True
for i in range(len(my_list)-1) :
    if my_list[i] > my_list[i+1] :
        ascending = False
        break
if ascending :
    print("\nList is sorted in ascending order\n")
else :
    print("\nList is not sorted in ascending order\n")
