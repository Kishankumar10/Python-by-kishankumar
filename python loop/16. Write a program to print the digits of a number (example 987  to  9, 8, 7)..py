##16. Write a program to print the digits
##of a number (example: 987 → 9, 8, 7).

a = input("enter a number:")
outcome = ""

for i in a:
    if outcome == "":
        outcome = i
    else:
        outcome = outcome + "," + i 
    
print(outcome)
 
