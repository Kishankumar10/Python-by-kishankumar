a = input("Enter the string : ")
result = ""
for i in a :
    if i == " ":
        result +=i
    elif i not in result :
        result += i 
print(result)