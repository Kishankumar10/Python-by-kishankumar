# 11. Write a program that finds the longest consecutive sequence in an unsorted list
#  of numbers using sets.

my_list = [11,4,10,1,3,2]

def longest_consecutive_sequence(num_list):
    check_set = set(num_list)
    largest = 0
    for i in check_set :
        if i-1 not in check_set:
            num = i
            count = 1
            while num + 1 in check_set :
                num += 1
                count += 1
            if count > largest :
                largest = count
    return largest

print(longest_consecutive_sequence(my_list))
    
        

                
                