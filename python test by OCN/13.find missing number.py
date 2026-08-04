# Numbers from 1 to N are given with one number
#  missing. Find the missing number.

a = [1, 2, 4, 5]
for i in range(1 , len(a) + 1) :
    if i not in a :
        print(i)
        break

