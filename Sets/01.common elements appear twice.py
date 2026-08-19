# 1. Given two lists, return the set of common elements that 
# appear more than once in both lists.


list_1 = [1,2,3,4,3,5,3,4]
list_2 = [3,4,5,4,6,3,7]
final_set = set()

common_elements = set(list_1) & set(list_2)

for i in common_elements :
    if list_1.count(i) > 1 and list_2.count(i) > 1 :
        final_set.add(i)
print(final_set)

