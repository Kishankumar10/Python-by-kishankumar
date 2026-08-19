# 15. Write a function that returns the elements in a set which are not present 
# in any of the other sets from a list of sets.

my_list = sets = [{1, 2, 3},{3, 4, 5},{5, 6, 1}]
# in dict keys can be integer

def unique_across_all_set(list_of_set):
    frequency = {}                   
    final_set = set()
    for num_set in list_of_set:
        for element in num_set :
            if element in frequency :
                frequency[element] += 1
            else :
                frequency[element] = 1
    for i in frequency.keys():
        if frequency[i] == 1 :
            final_set.add(i)
    return final_set
        
print(unique_across_all_set(my_list))

