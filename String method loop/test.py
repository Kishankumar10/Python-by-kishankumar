#LEGENDS CODE

a = input("Enter your string : ")
l = len(a)
result = ""
for i in range(l-1,-1,-1):
    result += a[i]
print(result)
