# 2. Dictionary Merging with Logic

# Practice Problem: Write a function that merges two dictionaries. 
# If a key exists in both dictionaries, sum their values. If a key 
# exists in only one, include it as is.

# version - 1 :

# dict_a = {'a': 10, 'b': 20} 
# dict_b = {'b': 5, 'c': 15}

# result = dict_a.copy()

# for i,j in dict_b.items() :
#     if i in dict_a :
#         result[i] += j
#     else:
#         result[i] = j
        
# print(result)

# version - 2 

dict_a = {'a': 10, 'b': 20} 
dict_b = {'b': 5, 'c': 15}

def merger(dict_1,dict_2) :
    result = dict_1.copy()
    for i,j in dict_2.items() :
        result[i] = result.get(i,0) + j
    return result 
        
print(merger(dict_a,dict_b))