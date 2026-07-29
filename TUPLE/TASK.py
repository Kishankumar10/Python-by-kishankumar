# 1. Create a tuple that contains an integer, a string, and a float.

a = (5897,"hello",21.35)

print(type(a))
print(type(a[0]))
print(type(a[1]))
print(type(a[2]))

# 2. Access the second element of the tuple (5, 10, 15, 20).
 
a = (5, 10, 15, 20)
print(a[1]) 

# 3.Slice the tuple (1, 2, 3, 4, 5) to get the last two elements.

a = (1, 2, 3, 4, 5)
print(a[3:])

# 4. Concatenate the tuples (1, 2) and (3, 4).

a = (1, 2)
b = (3, 4)
c = a + b 

print(c)

# 5. Repeat the tuple (7, 8) three times.

a = (7, 8)
print(a*3)

# 6. Check if 15 is present in the tuple (10, 20, 15, 25).

a = (10, 20, 15, 25)
print(15 in a)
print(type(15 in a))

# 7. Find the length of the tuple (3, 6, 9, 12).

a = (3, 6, 9, 12)                # print(len(a))
count = 0                      
for i in a :
    count += 1 
print(count)

# 8. Find the maximum and minimum values in the tuple (4, 1, 8, 3).

a = (4, 1, 8, 3)
maximum = a[0]                    # print(max(a))                                    
minimum = a[0]                     # print(min(a))
for i in a :
    if maximum < i :
        maximum = i             
    elif minimum > i :
        minimum = i 
print(maximum,"maximum")
print(minimum,"minimum")  

# 9. Convert the list [1, 2, 3, 4] into a tuple.

my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)
print(my_tuple)

# 10. Convert the tuple (10, 20, 30) into a list.

my_tuple = (10, 20, 30)
my_list = list(my_tuple)
print(my_list)

# 11. Find the index of the element 30 in the tuple (10, 20, 30, 40).

a = (10, 20, 30, 40)
print(a.index(30))

# 12. Count how many times 2 appears in the tuple (2, 3, 2, 4, 2).

a = (2, 3, 2, 4, 2)
print(a.count(2))

# 13. Unpack the tuple (100, 200, 300) into three separate variables.

a,b,c = (100, 200, 300)
print(a)
print(b)
print(c)

# 14. Swap the values of two tuples (1, 2) and (3, 4).

a = (1, 2)
b = (3, 4)

a,b = b,a

print(a)
print(b)

# 15. Create a tuple that contains two other tuples (1, 2) and (3, 4).

a = ((1, 2) , (3, 4))
print(a)
print(type(a[0]))
print(type(a[1]))

# 16. Access the number 4 from the nested tuple ((1, 2), (3, 4)).

a = ((1, 2), (3, 4))
print(a[1][1])

# 17. Find the sum of all numbers in the tuple (5, 10, 15).

a = (5, 10, 15)              # print(sum(a))
total = 0
for i in a :
    total += i
print(total)

# 18. Sort the elements of the tuple (40, 10, 30, 20) in ascending order.

my_tuple = (40, 10, 30, 20)
my_list = list(my_tuple)
my_list.sort()
my_tuple = tuple(my_list)
print(my_tuple) 


# 19. Reverse the elements of the tuple (1, 2, 3, 4, 5).

my_tuple = (1, 2, 3, 4, 5)                 

r = ()
for i in my_tuple :                    # reverse_tuple = my_tuple[::-1]
    r = (i,) + r                       # print(reverse_tuple)
print(r)

# 20. Check if all elements in the tuple (5, 5, 5, 5) are identical.

a = (5, 5, 5, 5)
identical = True
for i in range(1,len(a)) :
    if a[0] != a[i] :
        identical = False
        break

if identical : 
    print("The tuple is identical") 
else : 
    print("The tuple is not identical")
