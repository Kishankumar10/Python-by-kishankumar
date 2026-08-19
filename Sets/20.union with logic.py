# 20. Write a function that finds the union of all sets, but only includes elements 
# that appear more than once across all sets.

a = {1, 2, 3}
b = {2, 3, 4}
c = {3, 4, 5}

# version - 1 :
def union_frequency(*sets):
    if not sets :
        return set()
    union = set.union(*sets)
    final_set = set()
    for i in union:
        count = 0
        for num_set in sets:
            if i in num_set:
                count += 1
            if count == 2:
                final_set.add(i)
                break
    return final_set

print(union_frequency(a,b,c))

# version - 2 :

# def union_frequency(*sets):
#     count = {}
#     final_set = set()
#     for num_set in sets:
#         for element in num_set:
#             if element in count :
#                 count[element] += 1
#             else :
#                 count[element] = 1
#     for element in count.keys() :
#         if count[element] > 1:
#             final_set.add(element)
#     return final_set

# print(union_frequency(a,b,c))