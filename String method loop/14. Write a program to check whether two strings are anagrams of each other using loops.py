string_1 = input("Enter your first stirng : ").lower()
string_2 = input("Enter your second stirng : ").lower()

if len(string_1) != len(string_2) :
    print("they are not anagrams")
else:
    result = "they are anagrams"
    for i in string_1 :
        if string_1.count(i) != string_2.count(i) :
            result = "they are not anagrams"
    print(result)