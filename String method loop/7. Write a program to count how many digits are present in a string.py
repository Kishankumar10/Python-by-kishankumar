a = input("Enter your string : ")
count = 0
for i in a:
	if i.isdigit() :
		count +=1
print(f"The string '{a}' has {count} digits")