a = input("Enter your string : ")
vowels = ["a","e","i","o","u","A","E","I","O","U"]

for k in a:
	if k in vowels:
		a = a.replace(k,"*")
print(a)