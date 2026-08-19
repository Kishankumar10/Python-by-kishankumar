# def front_back(str):
#   front = str[0]
#   back = str[len(str)-1]
#   return (back + str[1:len(str)-1] + front)

# print(front_back('code'))
# def stupid(a,b,c):
#     return a+b+c
# print(stupid(5,6,4))

# def string_bits(str):
#     result = ""
#     for i in range(0,len(str),2):
#         result += str[i]
#     return result
# string_bits('Hello')

# def string_splosion(str):
#   result = ""
#   for i in range(1,len(str)+1):
#     result += str[:i]
#   return result
# print(string_splosion('Code'))

# a = 1
# b = 1
# print(id(a))
# print(id(b))
# print(a is b)

# def hello_name(name):
#     return (f"Hello {name}!")
# print(hello_name('Bob')) 

# def first_half(str):
#   return str[:len(str)//2]
# first_half('woohoo')


# def counter(n):
#     print(n)
#     if n == 1 :
#         return 
#     counter(n-1)
# counter(5)
# a = "global variable 1"
# b = "global variable 2"
# def test():
#     global a
#     a = "changed 1" 
#     b = "changed 2"
#     print(a)
#     print(b)
# test()
# print(a)
# print(b)


# a = "global "
# def outer():
#     a = "outer variable"
#     def inner():
#         nonlocal a
#         a = "inner variable"
#         def innermost():
#             nonlocal a 
#             a = "changed"
#         innermost()
#         print(a)
#     inner()
#     # print(a)
# outer()

# def countdown_count(n):
#     print(n)
#     if n == 1:
#         return 1
#     return 1 + countdown_count(n - 1)

# print(countdown_count(6))

# Recursive functoin 

# def factorial(num):
#     if num == 1 :
#         return 1 
#     return num * factorial(num - 1)
# print(factorial(5))
# a = [1,2,3]
# b = [4,8,6]
# print([a[1]]*3)

# def max_end3(nums):
#   if nums[0]>nums[-1]:
#     return [nums[0]]*3
#   return [nums[-1]]*3

# print(max_end3([1, 2, 3]) )
# print(len(a))
# mylist = [5,8,9,3,4]
# print({2,1} & set(mylist))
# print(bool({2,1}))

# print(range(1,9))

print(set(range(1,11)))