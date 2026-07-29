# 12. Write a Python program to replace all 
# negative numbers in a list with 0.

my_list = [6,-9,3,-1,8]

# VERSION-1
# index = 0
# for i in my_list :
#     if i < 0 :
#         my_list[index] = 0
#     index += 1
# print("\n",my_list,end = "\n\n")

# VERSION-2
for i in range(len(my_list)) :
    if my_list[i] < 0 :
        my_list[i] = 0
print("\n",my_list,end = "\n\n")
