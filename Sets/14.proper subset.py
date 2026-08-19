# 14. Write a function to determine whether a set is a proper 
# subset of another set.

a = {1,2,3,4,5,6}
b = {2,3,4}

# version - 1 :

# def proper_subset(superset,subset):
#     if superset == subset:
#         return False
#     for i in subset :
#         if i not in superset :
#             return False
#     return True

# version - 2 :

# def proper_subset(superset,subset):
#     return superset != subset and subset.issubset(superset)

# version - 3 :

def proper_subset(superset,subset):
    return superset > subset


if proper_subset(a,b) :
    print(f"{b} is a proper subset of {a}")
else :
    print(f"{b} is not a proper subset of {a}")