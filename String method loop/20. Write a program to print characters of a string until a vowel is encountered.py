a = input("Enter your string : ")
vowels = ["a","e","i","o","u","A","E","I","O","U"]
result = ""
continue_loop = True

for i in a:
    if continue_loop :
        if i not in vowels :
            result += i
        else :
            print(result)
            continue_loop = False