a = input("Enter your string : ").lower()
alpha_set =["a","b","c","d","e","f","g","h","i",
			"j","k","l","m","n","o","p","q","r",
			"s","t","u","v","w","x","y","z"]
     
if a == "":
    print("You entered no string")
else:
    result = "string contains only alphabetic characters"

    for i in a:
        if i not in alpha_set:
            result = "string contains non-alphabetic characters"

    print(result)