a = input("Enter your stirng : ")
count = 0
for i in a :
    if not(i.isalnum() or i==" "):
        count += 1
print(count)