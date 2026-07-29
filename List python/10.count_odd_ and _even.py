# 10. Write a Python program to count how many 
# even and odd numbers are present in a list.

my_list = [12,13,8,61,100]
even_count = 0 
for i in my_list : 
    if i%2 == 0 : 
        even_count += 1 
odd_count = len(my_list) - even_count
print(f"my_list has {even_count} even numbers")
print(f"my_list has {odd_count} odd numbers")