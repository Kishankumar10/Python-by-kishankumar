# 19. Write a Python program sorted in ascending order.
# Misinterpreted

my_list = [3,5,6,4,1,2]
new_list = []
smallest_number = my_list[0]
for k in range(len(my_list)):
    for i in my_list :
        if i < smallest_number :
            smallest_number = i 
    new_list.append(smallest_number)
    my_list.remove(smallest_number)
    if my_list != [] :
        smallest_number = my_list[0] 
print(new_list)      