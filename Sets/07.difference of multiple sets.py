# 7. Find the set difference of multiple sets.

a = {1,2,3,4,5}
b = {4,5,6}
c = {2,7}

# version - 1 :

# def multiple_difference(first = None , *sets):
#     if first is None:
#         return set()
#     final_set = first.copy()
#     for i in sets :
#         final_set.difference_update(i)
#     return final_set

# version - 2 :

def multiple_difference(first = None , *sets):
    if first is None:
        return set()
    return first.difference(*sets)

print(multiple_difference(a,b,c))