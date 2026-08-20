my_list = ["1","2","3","4","5"]

# int_ = map(int,my_list)
# int_list = list(int_)

# def square(a) :
#     return a * a

# square_result = map(square,int_list)
# print(list(square_result),"by normal function")

# lambda_square = map(lambda a : a * a , int_list)
# print(list(lambda_square),"by lambda function")

int_list = map(int, my_list)

print(list(int_list), "first print")
print(list(int_list), "second print")