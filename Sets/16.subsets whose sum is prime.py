# 16. Find all possible subsets of a set and return the ones
#  where the sum of elements is prime.

my_set = {1,2,3,4}
def all_subset_generator(given_set):
    my_list = [set()]
    prime_sum_subset = []
    for element in given_set :
        copy_list = my_list.copy()
        for old_subsets in copy_list :
            my_list.append(old_subsets|{element})
    for subset in my_list :
        subset_sum = sum(subset)
        if subset_sum <= 1 :
            continue
        is_prime = True
        for i in range(2, subset_sum):
            if subset_sum % i == 0:
                is_prime = False
                break
        if is_prime :
            prime_sum_subset.append(subset)
    return prime_sum_subset

print(all_subset_generator(my_set))

# we can improve later