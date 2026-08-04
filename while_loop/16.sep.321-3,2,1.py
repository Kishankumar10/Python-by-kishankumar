# 16. Write a program to print the digits of a number (example: 987 → 9, 8, 7).
a = int(input("Enter a number : "))
div = 10 ** (len(str(a))-1)
result = ""
while div > 0 :
    first_digit = str(a // div)
    a %= div
    div //= 10
    if result == "" :
        result += first_digit
    else :
        result += "," + first_digit
print(result)
 