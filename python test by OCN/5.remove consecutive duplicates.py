# remove consecutive duplicates

a = "aaabbbcca"
result = a[0]
for i in range(1,len(a)):
    if a[i] != a[i-1] :
        result += a[i]
print(result)
        


    
