# 1) Swap Two Elements at Given Indices - Write a script to swap the positions of two elements in a list based on their indices.


# Given Input:

# List: [23, 65, 19, 90]
# Indices to Swap: 0 and 2


# Expected Output:

# Original: [23, 65, 19, 90]
# Swapped: [19, 65, 23, 90]


my_list = [23, 65, 19, 90]

def swap(a,b,num_list):
    first_pos = num_list[a]
    num_list[a] = num_list[b]
    num_list[b] = first_pos

swap(0,2,my_list)
print(my_list)