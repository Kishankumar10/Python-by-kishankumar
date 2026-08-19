# 8. Given a list of sets, write a program to return the set containing 
# elements that are present in every set in the list.

# Elements present in all: 2, 3
my_list = [
    {1, 2, 3, 4},
    {2, 3, 5, 6},
    {3, 7, 2, 8}
]

def element_in_all_set(list_set=None):
    if list_set is None or list_set == []:
        return set()
    return list_set[0].intersection(*list_set[1:])

print(element_in_all_set(my_list))


    