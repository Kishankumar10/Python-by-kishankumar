# sum of digits

a = int(input())
total = 0
while a > 0 :
    last_digit = a % 10
    total += last_digit
    a //= 10
print(total)
    