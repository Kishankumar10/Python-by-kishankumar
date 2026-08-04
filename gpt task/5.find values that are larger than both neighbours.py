# Find all values that are larger than both neighbours.
a = (3,7,2,8,6,5)

found = False
for i in range(1,len(a)-1):
    if a[i-1] < a[i] and a[i] > a[i+1]:
        print(a[i])
        found = True
        
if not found :
    print("no item satisfy the condition")
    
