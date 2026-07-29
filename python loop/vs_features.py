# for i in range(1,21):
#     if i%5 == 0 and i%3 == 0 :
#         print("FizzBuzz")
#     elif i%3 == 0 :
#         print("Fizz")
#     elif i%5 == 0 :
#         print("Buzz")
#     else :
#         print(i)
# a = "hello"
# b = "hello" 
# print(a is b)

# identity operator ( is , is not )

a1 = [1,2,3]
a2 = [1,2,3]
a3 = a1
print(a1 == a2," identity")
print(a1 is a2 ," identity")
print(a1 is a3 ," identity")
print( a1 is not a2)