a = input("Enter your string : ")

lower_list = ["a","b","c","d","e","f","g","h","i",
              "j","k","l","m","n","o","p","q","r",
              "s","t","u","v","w","x","y","z"]
upper_list = ["A","B","C","D","E","F","G","H","I",
              "J","K","L","M","N","O","P","Q","R",
              "S","T","U","V","W","X","Y","Z"]

first_letter = a[0]
if (first_letter in upper_list) and (first_letter not in lower_list) and not(first_letter.isalpha()):
    print(a)
else:
    lower_position = lower_list.index(first_letter)
    cap_letter = upper_list[lower_position]
    a = a.replace(first_letter,cap_letter,1)
    print(a)

