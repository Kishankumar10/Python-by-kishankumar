##Write a program to determine whether a number is a palindrome.

a = input("enter a number:")
count = len(a)
result = "palindrome"

inter = 0
stop_codon = count//2

for k in a:
    inter += 1
    if inter <= stop_codon:
        if k != a[-inter]:
            result = "not palindrome"
            break

print(result)
