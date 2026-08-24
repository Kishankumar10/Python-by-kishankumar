# Check whether any two numbers in a list add up to the target value.

# Version - 1 

# a = [2, 7, 11, 15]
# sum_add = False
# target = 9
# match_gate = False
# for i in a :
#     if match_gate :
#         break
#     for j in a :
#         if  i + j == target :
#             sum_add = True
#             match_gate = True
#             break
# print(sum_add)

# Version - 2 

a = [2, 7, 11, 15]
target = 9
sum_add = False
match_gate = False

for i in a :
    if match_gate :
        break
    for j in a[a.index(i)+1:] :
        if i + j == target :
            sum_add = True
            match_gate = True
            break

print(sum_add)

# version - 3 

a = [2, 7, 11, 15]
target = 9
sum_add = False
match_gate = False

for i in range(len(a)) :
    if match_gate :
        break
    for j in a[i+1:] :
        if a[i] + j == target :
            sum_add = True
            match_gate = True
            break

print(sum_add)