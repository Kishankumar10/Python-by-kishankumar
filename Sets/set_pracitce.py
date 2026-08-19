# mySet = {"a","b","c","d"}
# print(type(mySet))
# print(mySet)

# # adding elements

# mySet.add("z")
# print(mySet,"after adding")







# mySet = { 1,2,3,4,5,6,7,8,9,10,5}
# print(type(mySet))
# print(mySet)

# unordered, unidexed, does not allow duplicates,mutable
# set1 = {"aaa","bbb","ccc","ddd"}
# print(set1)
# print(len(set1))

# for i in set1:
#     print(i)

# a={1,2,3,4}
# b={2,6,4}
# b.intersection_update(a)
# print(b)

# # difference
# a = {1,2,3,4}
# b = {3,4,5,6}

# a.symmetric_difference_update(b)
# print(a)

#isdisjoint

# a = {1,2,3}
# b = {5,4,6}

# print(a.isdisjoint(b))


# #issubset
# #true statement
# a = {1,2,3}
# b = {1,2,3,4,5}

# print(a.issubset(b))
#  #false statement
# c = {1,2,3}
# d = {2,3,4,5}
# print(c.issubset(d))


#issuperset

# a = {1,2,3,4,}
# b = {1,5}

# print(a.issuperset(b))


# a = {1,2,3}
# b = {3,4,5}

# c = a.update(b)
# print(a)
# print(b)
# print(c)

# a = {1,2,3}
# b = {3,4,5}

# c = a.intersection(b)
# print(a)
# print(b)
# print(c)
# a = set([1,2,3,4,5,6])
# print(a)
# print(type(a))
# a = {1,2,3,4,5,6}
# a.clear()
# print(a)
# a = {1,2,3,4,5,6}
# print(a.intersection(*[]))

# dictionary = {
#     3 : "element",
#     4 : "haha"
# }
# print(dictionary[3])

# 4 = "hello"
# print(0)



# version - 2 :

# my_list = ["A","B","C"]

# def permutations_generator(List) :
#     perm= [List[0]]
#     for element in List[1:]:
#         for comb in perm.copy() :
#             replace_list = []
#             for i in range(len(comb) + 1) :
#                 replace_list.append(comb[:i] + element + comb[i:])
#             perm.remove(comb)
#             perm.extend(replace_list)
            
#     return perm

# print(permutations_generator(my_list))

mySet = {1,2,3,4}
print(sum(mySet))