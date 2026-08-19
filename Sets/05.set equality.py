# 5. Check if two sets are equal, considering their elements but 
# ignoring the order (i.e., set equality).

a = {1,2,3,4,5,6}
b = {1,5,4,6,2,3}


def set_equality(set_1,set_2):
    if len(set_1) != len(set_2) :
        return False
    for i in set_1:
        if i not in set_2:
            return False
    return True

print(set_equality(a,b))


