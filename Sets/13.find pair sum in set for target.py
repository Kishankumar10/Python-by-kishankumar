# 13. Write a function that checks if there exists a pair of 
# numbers in a set that sum to a specific target.

my_set = {6,4,8,2,3,1,7}
num = 4

# version - 1 :

# def pair_sum_finder(set_num,target):
#     for i in set_num :
#         for j in set_num :
#             if i != j and i + j == target :
#                 return True 
#     return False

# version - 2 :

def pair_sum_finder(set_num,target):
    for i in set_num :
        sub_value = target - i
        if sub_value != i and sub_value in set_num:
            return True
    return False

print(pair_sum_finder(my_set,num))