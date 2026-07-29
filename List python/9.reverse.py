# 9. Write a Python program to reverse a list
# without using the .reverse() method.

my_list = [11,22,33,44,55]

# print("Method-1")
# reverse_list = my_list[::-1]

# print("Method-2") 
# reverse_list = []
# for i in my_list :
#     reverse_list.insert(0,i)

# print("Method-3") 
reverse_list = []
for i in range (len(my_list)-1,-1,-1) :
    reverse_list.append(my_list[i])


print(reverse_list)



