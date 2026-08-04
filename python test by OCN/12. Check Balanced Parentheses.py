# Check Balanced Parentheses

a = "(()())"
# opening_parentheses = a.count("(")                  # wrong
# closing_parentheses = a.count(")")
# print(opening_parentheses == closing_parentheses)

balance = 0
for i in a :
    if i == "(" :
        balance += 1
    elif i == ")" :
        balance -= 1
    if balance < 0 :
        break 
print(balance == 0)