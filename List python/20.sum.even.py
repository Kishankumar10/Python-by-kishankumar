# 20. Write a Python program to find the sum
# of only the even numbers in a list.

my_list = [12,5,9,62,51,100]
total = 0 
for i in my_list :
    if i%2 == 0 :
        total += i
print(f"\nSum of even form list : {total}\n")        