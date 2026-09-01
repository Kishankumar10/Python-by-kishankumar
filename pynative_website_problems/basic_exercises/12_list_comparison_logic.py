# 12. List Comparison and Boolean Logic

# Practice Problem: Write a function to return True if the first and last number of a given list is the same. If the numbers are different, return False.

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

def compare_first_last(lst):
    return lst[0] == lst[-1]

print(compare_first_last(numbers_x))
print(compare_first_last(numbers_y))