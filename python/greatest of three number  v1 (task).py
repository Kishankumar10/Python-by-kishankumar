#greatest of three numbers 

a=int(input('enter your first number:'))
b=int(input('enter your second number:'))
c=int(input('enter your third number:'))

if a>b:
    greater_number = a
	
else:
    greater_number = b
	
	
if greater_number > c:
    print(greater_number)
	
else:
    print(c)
	
print('is your greatest number')

