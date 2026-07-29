a = input("Enter your string : ").lower()

consonants = ["b","c","d","f","g","h","j",
			  "k","l","m","n","p","q","r",
			  "s","t","v","w","x","y","z"]
count = 0
for k in a:
	if k in consonants:
		count += 1
print(count)