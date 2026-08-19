# 17. Create a set of all permutations of a given list of characters.

# version - 1  (not scalable) :

# my_list = ["A","B","C"]
# final_set = set()

# for i in my_list :
#     remaining = my_list.copy()
#     remaining.remove(i)
#     for direction in (1,-1):
#         constructor = i 
#         for j in remaining[::direction]:
#             constructor += j
#         final_set.add(constructor)

# print(final_set)


# version - 2 : (dynamic version)

my_list = ["A","B","C","D"]

def permutations_generator(List) :
    perm= [List[0]]
    for element in List[1:]:
        for comb in perm.copy() :
            replace_list = []
            for i in range(len(comb) + 1) :
                replace_list.append(comb[:i] + element + comb[i:])
            perm.remove(comb)
            perm.extend(replace_list)
    return set(perm)

print(permutations_generator(my_list))