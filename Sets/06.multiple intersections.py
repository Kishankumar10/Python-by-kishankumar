# 6. Write a program that finds the intersection of multiple sets.
a = {1,2,3,4,5,6}
b = {2,3,4,6}
c = {9,2,3,4,7}

# version - 1 :

# def multiple_intersection(*sets):
#     if not sets :                    # print(bool()) gives False
#         return set()
#     final_set = sets[0].copy()       # 'a' set not get modified
#     for i in sets[1:] :
#         final_set.intersection_update(i)
#     return final_set

# version - 2 :

def multiple_intersection(first = None,*sets):
    if first is None:
        return set()
    return first.intersection(*sets)

print(multiple_intersection(a,b,c)) 





