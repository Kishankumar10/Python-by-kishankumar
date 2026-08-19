# 19. Find the number of elements that appear in exactly one set from a list of sets.
my_list = [{1, 2, 3}, {3, 4, 5}, {5, 6, 1}]

def count_unique_to_one_set(list_of_set):
    frequency = {}
    count = 0
    for num_set in list_of_set:
        for element in num_set :
            if element in frequency :
                frequency[element] += 1
            else :
                frequency[element] = 1
    for i in frequency.values():
        if i == 1 :
            count += 1
    return count

print(count_unique_to_one_set(my_list))
    
