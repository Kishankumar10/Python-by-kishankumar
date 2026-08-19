# 18. Check if a set contains a subset of elements that sum up to a specific value.

my_set = {2, 3, 5, 7}
my_number = 10

def subset_sum_target(given_set,target):
    my_list = [0]
    condition = False
    for element in given_set :
        for subset_sum in my_list.copy() :
            new_sum = subset_sum + element
            if new_sum == target :
                condition = True
                break
            my_list.append(new_sum)
        if condition :
            break 
    return condition

print(subset_sum_target(my_set,my_number))
