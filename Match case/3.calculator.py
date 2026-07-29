# 3. Create a *simple calculator* that performs
# addition, subtraction, multiplication, or division
# based on user input using match.

a = int(input("Enter first number : "))
operator = (input("Enter the arithmetic operator : "))
b = int(input("Enter second number : "))
match operator :
    case "+" :
        print(f"{a} + {b} = {a+b}") 
    case "-" :
        print(f"{a} - {b} = {a-b}")
    case "*" :
        print(f"{a} * {b} = {a*b}") 
    case "/" :
        print(f"{a} / {b} = {a/b}")
    case _ :
        print("Enter valid operator")          