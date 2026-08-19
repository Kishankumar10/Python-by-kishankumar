# # Manual Sorting
# Version - 1:

# my_list = [3,5,6,4,1,2]
# new_list = []
# smallest_number = my_list[0]
# for k in range(len(my_list)):
#     for i in my_list :
#         if i < smallest_number :
#             smallest_number = i 
#     new_list.append(smallest_number)
#     my_list.remove(smallest_number)
#     if my_list != [] :
#         smallest_number = my_list[0] 
# print(new_list) 

# ----------------------------------------------------------------------------
# Manual Sorting
# Version - 2 :

# a = (3,5,6,4,1,2)
# sort = list(a)
# small = sort[len(a) - 1]
# for i in range(len(a)) :
#     for j in sort[i:] :
#         if j < small :
#             small = j 
#     p = sort.index(small)                
#     sort[i] , sort[p] = small , sort[i]
#     small = sort[len(a)-1]
    
# print(sort)

# ----------------------------------------------------------------------------
# Manual Sorting
# Version - 3 :

a = [3,5,6,4,1,2]
for i in range(len(a)) :
    small_index = i
    for j in range(i+1 , len(a)) :
        if a[j] < a[small_index] :
            small_index = j
    a[i] , a[small_index] = a[small_index] , a[i]
print(a)
