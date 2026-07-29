##15. Write a program to reverse a number
##using a for loop (example: 1234 → 4321).

given_number = input("enter the number to be reversed :")
reversed_number = ""

for i in given_number:
    reversed_number = i + reversed_number
   #reversed_number += i (prints number forward )

print(reversed_number)
    
    
