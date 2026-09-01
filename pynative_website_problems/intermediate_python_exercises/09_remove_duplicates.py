# 9. Remove Duplicates (Preserving Order)

# Practice Problem: Write a function that removes duplicate elements from a list. You cannot use set() because sets do not maintain the original order of elements.

my_list = [1, 2, 2, 3, 1, 4, 2]

def remove_duplicates_ordered(num_lst):
    seen = set()
    result = []
    for i in num_lst:
        if i not in seen:
            seen.add(i)
            result.append(i)
    return result 

print(remove_duplicates_ordered(my_list))