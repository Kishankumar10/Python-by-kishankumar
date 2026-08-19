# 3. Write a function that takes a list of numbers and returns the largest subset 
# such that the sum of the subset is even.

my_list = [1,2,3,4,5]
def largest_subset_with_sum_to_even(given_list):
    subset_list = [set()]
    for element in given_list :
        for old_subsets in subset_list.copy() :
            subset_list.append(old_subsets|{element})
    for subset in subset_list[::-1] :
        if sum(subset) % 2 == 0 :
            return subset


print(largest_subset_with_sum_to_even(my_list))