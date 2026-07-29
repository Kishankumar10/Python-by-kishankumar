##8. Write a program to find the sum of even numbers from 1 to 20.

total = 0
for i in range(1,21):
    if i%2==0:
        total += i
print(total)
