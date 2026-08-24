# Find Second Largest Number
my_list = [10, 5, 20, 8, 20]
if my_list[0] > my_list[1] :
    largest = my_list[0]
    second_largest = my_list[1]
else :
    largest = my_list[1]
    second_largest = my_list[0]
for i in my_list[2:] :
    if i > largest :
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest :
        second_largest = i
print(f"\nThe second largest number is '{second_largest}'\n")