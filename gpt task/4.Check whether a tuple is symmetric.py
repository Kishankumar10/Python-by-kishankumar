# Check whether a tuple is symmetric, Do it without reversing the tuple.
a = (1,2,3,2,1)
symmetric = True 
for i in range(len(a)//2):
    if a[i] != a[-i-1]:
        symmetric = False
        break 
if symmetric :
    print("Tuple is symmetric")
else:
    print("Tuple is not symmetric")

        
