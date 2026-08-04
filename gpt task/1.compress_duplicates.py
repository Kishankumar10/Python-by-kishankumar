# Compress consecutive duplicates.

#verion - 1

# a = (1,1,1,2,2,3,3,3,1)    # output = (1,2,3,1)
# b = []
# for i in range(len(a)) :
#     if i != (len(a)-1) :     # to not to allow last to avoid index error
#         if a[i] == a[i+1] :  # compare next element 
#             continue         # if it same then skip the append
#         b.append(a[i])
#     else :
#         b.append(a[i])       # the last rejected element is added 
# print(tuple(b))

#------------------------------------------------------------------------------#
# Compress consecutive duplicates.
#version-2
     
a = (1,1,1,2,2,3,3,3,1)
b = []
for i in range(len(a)):
    if i == (len(a)-1) or a[i] != a[i+1] :
        b.append(a[i])
print(tuple(b))
#------------------------------------------------------------------------------#
# mirror algorithum version 

# a = (1,1,1,2,2,3,3,3,1)
# b = []
# for i in range(len(a)) :
#     if i == 0 or a[i] != a[i-1] :
#         b.append(a[i])
# print(tuple(b))