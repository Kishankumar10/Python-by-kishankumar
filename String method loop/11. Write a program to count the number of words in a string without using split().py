a = input("Enter your string : ").strip()
if a == "" :
    count = 0
else:
    count = 1
    for i in a :
        if i == " ":
            count += 1
print(count)