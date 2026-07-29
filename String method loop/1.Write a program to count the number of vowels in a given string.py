a = input("Enter your string : ")
b = a.lower()
vowels = ["a","e","i","o","u"]
count = 0
for k in b:
	if k in vowels:
		count += 1
print(f"The string '{a}' has {count} vowels")
