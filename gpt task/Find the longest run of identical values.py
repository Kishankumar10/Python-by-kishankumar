# Find the longest run of identical values

a = (1,1,2,2,3,3,3)           # answer = 3
count = 1
longest_run = 0
for i in range(len(a)) :
    if i != (len(a)-1) and a[i] == a[i+1] :
        count += 1
    else :
        if  count > longest_run :
            longest_run = count
        count = 1
print(longest_run)





