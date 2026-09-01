# 14. Subset and Superset Validation

# Practice Problem: Write a script that takes two lists of integers from a user, converts them to sets, and determines if the first set is a Subset, a Superset, or Disjoint from the second.

set_a = [1, 2, 3]
set_b = [1, 2, 3, 4, 5]

def validate_relationships(list1, list2):
    set_1 = set(list1)
    set_2 = set(list2)
    if set_1 == set_2:
        print("both are same set")
    elif set_1 < set_2:
        print("set A is a subset of set B")
    elif set_1 > set_2:
        print("set A is a superset of set B")
    elif set_1.isdisjoint(set_2):
        print("sets are disjoint (so they share no common elements)")
    else:
        print(f"The sets share these elements: {set_1 & set_2}")


validate_relationships(set_a, set_b)