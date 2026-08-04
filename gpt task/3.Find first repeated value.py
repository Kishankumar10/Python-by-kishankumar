# Find the first repeated value.

# a = tuple(map(int,input("Enter the values with spaces : ").split()))
a = (5,4,9,3,1,5,9,1)
b = []
for i in a :
    if i in b :
        print(f"{i} is the first repeated value")
        break 
    b.append(i)
else :
    print("the given values has no repeated value")
    