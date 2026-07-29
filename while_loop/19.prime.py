a = int(input("Enter the number : "))
if a < 2 :
    print("it is  not a prime number")
else:
    i = 2
    result = "it is a prime number" 
    while i < a :
        if a%i == 0 :
            result = "it is not a prime number"
            break
        i += 1
    print(result)
    

    