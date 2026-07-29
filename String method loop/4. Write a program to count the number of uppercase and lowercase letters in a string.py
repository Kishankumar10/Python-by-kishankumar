a = input("Enter the string : ")
uppercase = 0
lowercase= 0 

for i in a:
    if i.isupper():
        uppercase += 1 
    elif i.islower(): 
        lowercase += 1 

print(f"The string {a} has {uppercase} uppercase letters.")
print(f"The string {a} has {lowercase} lowercase letters.")
