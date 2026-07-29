a = input("Enter your string : ") 
b = a.lower()
result = ""
for i in b :
	result = i + result
if result == b:
	print(f"{a} is a palindrome")
else :
	print(f"{a} is not a palindrome")