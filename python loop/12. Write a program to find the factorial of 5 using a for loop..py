##12. Write a program to find the factorial of 5
##using a for loop.

a = int(input("enter a number to find its factorial:"))

factorial = 1
        
for i in range(1,a+1):
    factorial *= i
        
print(f"the factorial of {a} is {factorial}")
    
