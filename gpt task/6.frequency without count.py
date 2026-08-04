# Frequency Without count()
a = (1,2,1,3,2,1)
b = []
for i in a :
    count = 0
    if i in b :
        continue
    for n in a :
        if i == n :
            count += 1
    print(f"frequency of '{i}' is {count}")
    b.append(i) 

