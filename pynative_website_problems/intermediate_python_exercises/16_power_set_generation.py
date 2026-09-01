# 16: Power Set Generation

# Practice Problem: Write a function that generates the Power Set of a given set (a set of all possible subsets, including the empty set and the set itself).

from itertools import combinations

my_set = [1,2,3,4,5]

def get_power_set(collections):
    return [items 
            for r in range(len(collections)+1)
            for items in combinations(collections,r)]

print(get_power_set(my_set))