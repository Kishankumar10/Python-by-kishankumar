# 15: Set Symmetric Difference

# Practice Problem: Given two lists of student IDs, find the IDs that appear in either the first or the second list, but not in both.

list1 = [101, 102, 103]
list2 = [103, 104, 105]

def symmetric_diff(lst1,lst2):
    a = set(lst1)
    b = set(lst2)
    return a ^ b

print(symmetric_diff(list1,list2))