##19. Write a program to check if a number is prime or not using a for loop.

a = int(input("enter your number:"))

##It is a natural number (positive integer: 1, 2, 3...).
##It is greater than 1.
##It can only be divided evenly
 #by exactly two numbers: 1 and itself
if a<=1 :
    print("it is a not prime number")
else:    
    is_prime = "it is a prime number"

    for i in range(2, a):
        if a % i == 0:
           is_prime ="it is not a prime number"
    print(is_prime)
    

 

        

