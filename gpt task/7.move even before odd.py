# Move every even number before every odd number.

# Version - 1 :

# a = (5,8,2,1,6,7)     # result = (8,2,6,5,1,7)
# b = list((5,8,2,1,6,7))
# for i in a :
#     if i % 2 != 0 :
#         b.remove(i)
#         b.append(i)
# print(tuple(b))       
          
# Version - 2 :

a = (5,8,2,1,6,7)
odd = []
even = []
for i in a :
    if i % 2 == 0 :
        even.append(i)
    else :
        odd.append(i)
print(tuple(even + odd))
