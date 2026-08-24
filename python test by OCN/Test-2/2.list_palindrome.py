# 2) Check if List is Palindrome - Determine if a list reads the
#  same forward and backward. The function should return True
#  if it is a palindrome and False otherwise.

# Given Input: List: [1, 2, 3, 2, 1]

# Expected Output: Is Palindrome: True

my_list = [1, 2, 3, 2, 7]

def palindrome(num_list):
    middle = len(num_list)//2
    result = True 
    for i in range(middle):
        if num_list[i] != num_list[-1-i]:
            result = False
            break 
    return result
            
print(palindrome(my_list))