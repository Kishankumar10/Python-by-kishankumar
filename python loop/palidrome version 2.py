# palidrome version-2 iteration 

a = input("Enter the number to check wheather it is palidrome or not :")
length = len(a)     # to calculate the length of given number
stopper = length//2  # used to stop the loop half way to number 
result = True      # we are the considering the given number as a palidrome
for i in range(stopper):
    if a[i] != a[-1-i]:
        result = False
        break
# decalring out output
if result :
    print(f"The number {a} is a palidrome")
else :
    print(f"The number {a} is not a palidrome")

