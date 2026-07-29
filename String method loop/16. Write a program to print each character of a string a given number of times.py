a = input("Enter your stirng : ")
b = int(input("how many times to print : "))

for i in a:
    result = ""
    for j in range(b) :
        result += i
    print(result)
    