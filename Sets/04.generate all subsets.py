# 4. Given a set of integers, write a function that returns a new set containing 
# all subsets of the original set.

my_set = {1,2,3,4}
def all_subset_generator(given_set):
    my_list = [set()]
    for element in given_set :
        for old_subsets in my_list.copy() :
            my_list.append(old_subsets|{element})
    return my_list

print(all_subset_generator(my_set))

# a set can't have a set 
# TypeError: cannot use 'set' as a set element (unhashable type: 'set')












# Set: {A, B, C}

#                 Start: [ ]
#                /          \
#          Keep A            Skip A
#          /    \            /    \
#      Keep B   Skip B   Keep B   Skip B
#      /   \    /   \    /   \    /   \
#     C     _  C     _  C     _  C     _   <-- (Decide for C)
#     |     |  |     |  |     |  |     |
#  {A,B,C} {A,B} {A,C} {A} {B,C} {B}  {C}  {}