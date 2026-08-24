# Find maximum difference

a = [4, 7, 2, 9, 1]
# print(max(a) - min(a))
big_num = a[0]
small_num = a[0]
for i in a[1:] :
    if i > big_num :
        big_num = i 
    elif i < small_num :
        small_num = i
print(big_num - small_num)