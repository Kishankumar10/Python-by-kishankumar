# 17. Write a Python program to count how many 
# numbers in a list are divisible by 5.

my_list = [12,15,45,26,7,9,10]
count = 0
for i in my_list :
    if i%5 == 0 :
        count += 1
print(f"\n{count} items in the list are divisible by 5\n")
    