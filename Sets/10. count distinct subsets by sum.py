# 	10. Given a set, find the number of distinct subsets where the sum of the elements 
# in each subset is divisible by a given integer.

# version - 1

# my_set = {1, 2, 3, 4}
# target = 3

# def count_divisible_subset_sums(given_set,divisor):
#     subset_list = [set()]
#     for element in given_set :
#         for old_subsets in subset_list[:] :
#             subset_list.append(old_subsets|{element})
#     count = 0
#     for subset in subset_list :
#         if sum(subset) % divisor == 0 :
#             count += 1
#     return count

# print(count_divisible_subset_sums(my_set,target))
        
# version - 2 : (sum list collection)

# my_set = {1, 2, 3, 4}
# target = 3

# def count_divisible_subset_sums(given_set,divisor):
#     sum_list = [0]
#     for element in given_set :
#         copy_list = sum_list.copy()
#         for subset_sum in copy_list:
#             sum_list.append(subset_sum + element)
#     count = 0
#     for i in sum_list :
#         if i % divisor == 0 :
#             count += 1
#     return count

# print(count_divisible_subset_sums(my_set,target))

# version - 3  (even more compression of stored data)

my_set = {1, 2, 3, 4}
target = 3

def count_divisible_subset_sums(given_set,divisor):
    sum_list = [0]
    count = 1 
    for element in given_set :
        copy_list = sum_list.copy()
        for subset_sum in copy_list:
            remainder = (subset_sum + element) % divisor
            if remainder == 0 :
                count += 1
            sum_list.append(remainder)
    return count

print(count_divisible_subset_sums(my_set,target))