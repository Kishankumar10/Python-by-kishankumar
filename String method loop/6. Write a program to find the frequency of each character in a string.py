Input = input("Enter your string : ")
a = Input.lower()
b = a.strip()
c = ""
for i in b:
    if i not in c:
        c += i
        counter = b.count(i)
        print(f"The frequency of character {i} is {counter}")