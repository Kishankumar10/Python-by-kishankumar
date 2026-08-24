# Compress repeated characters by showing each character 
# followed by its count.

a = "aaabbc"           #a3b2c1
result = ""
count = 1
for i in range(len(a)):
    if i == (len(a)-1) or a[i] != a[i+1] :
        result += a[i] + str(count)
        count = 1
    else :
        count += 1
print(result)

