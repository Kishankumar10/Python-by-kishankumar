# Character frequency
a = "banana"
b = ""
for i in a :
    count = 0
    if i in b :
        continue
    for n in a :
        if i == n :
            count += 1
    print(f"frequency of '{i}' is {count}")
    b += i 