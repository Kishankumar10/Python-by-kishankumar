# 1. Arithmetic Product and Conditional Logic

# Practice Problem: Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.



def multiplication_or_sum(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    return num1 + num2

print(multiplication_or_sum(20, 30))
print(multiplication_or_sum(40, 30))