# 15. Write a Python program to print all 
# duplicate values in a list.
my_list = [2,4,2,5,6,5,8,1,8,8,9,8,8,8]

# VERSION - 1

check_list = []
print_list = []
for i in my_list :
    if i in check_list and i not in print_list :
        print(i)
        print_list.append(i)
    check_list.append(i)

# VERSION - 2

# check_list = []
# for i in my_list :
#     if i not in check_list and my_list.count(i) > 1 :
#         print(i)
#     check_list.append(i)



