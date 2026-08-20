from functools import reduce

# 1. Double All Numbers

# my_list = [1, 2, 3, 4, 5]

# double_list = map(lambda a : a * 2, my_list)
# print(list(double_list),"double_list")

# 2. Square All Numbers

# my_list = [2, 3, 4, 5]

# square_list = map(lambda a : a * a, my_list)
# print(list(square_list),"square_list")

# 3. Convert Strings to Integers

# my_list = ["10", "20", "30", "40"]

# int_list = map(int , my_list)
# print(list(int_list),"int_list")



# 4. Convert Names to Uppercase

# my_list = ["john", "alice", "bob"]

# upper_list = map(lambda a : a.upper(),my_list)
# print(list(upper_list),"upper_list")

# 5. Find Length of Each Word

# my_list = ["apple", "banana", "kiwi"]

# len_list = map(lambda a : len(a), my_list)
# print(list(len_list),"len_list")

# 6. Filter Even Numbers

# my_list = [1, 2, 3, 4, 5, 6]

# even_list = filter(lambda a : a % 2 == 0, my_list)
# print(list(even_list),"even_list")

# 7. Filter Odd Numbers

# my_list = [1, 2, 3, 4, 5, 6]

# odd_list = filter(lambda a : a % 2 != 0, my_list)
# print(list(odd_list),"odd_list")

# 8. Filter Positive Numbers

# my_list = [-5, -2, 0, 3, 8]

# positive_list = filter(lambda a : a > 0, my_list)
# print(list(positive_list),"positive_list")

# 9. Filter Words Longer Than 4 Characters

# my_list = ["cat", "elephant", "dog", "tiger"]

# longer4_word_list = filter(lambda word : len(word) > 4, my_list)
# print(list(longer4_word_list),"longer4_word_list")

# 10. Extract Vowels from a String

# my_string = "programming"

# vowels_list = filter(lambda a : a in "aeiou", my_string)
# print(list(vowels_list,"vowels_list"))

# 11. Sum of All Numbers

# my_list = [1, 2, 3, 4, 5]

# sum_value = reduce(lambda acc , curr : acc + curr , my_list)
# print(sum_value,"sum_value")

# 12. Product of All Numbers

# my_list = [1, 2, 3, 4]

# product_value = reduce(lambda acc , curr : acc * curr , my_list)
# print(product_value,"product_value")

# 13. Find Maximum Number

# my_list = [4, 10, 7, 25, 3]

# def max_finder(acc, curr):
#     if acc > curr :
#         return acc
#     return curr
# max_num = reduce(max_finder, my_list)
# # max_num = reduce(lambda acc , curr : acc if acc > curr else curr , my_list)
# print(max_num,"max_num")

# 14. Find Minimum Number

# my_list = [4, 10, 7, 25, 3]

# def min_finder(acc, curr):
#     if acc < curr :
#         return acc
#     return curr
# min_num = reduce(min_finder, my_list)
# # min_num = reduce(lambda acc , curr : acc if acc < curr else curr , my_list)
# print(min_num,"max_num")

#  15. Join Words into a Sentence

# my_list = ["Python", "is", "awesome"]

# def sentence_maker(sen, word):
#     return sen + " " + word
# sentence = reduce(sentence_maker, my_list)
# # sentence = reduce(lambda sen, acc : sen + " " + acc, my_list)
# print(sentence,"sentence")

# 16. Square Only Even Numbers

# my_list = [1, 2, 3, 4, 5, 6]

# # even_list = filter(lambda a : a % 2 == 0, my_list)
# # square_even = map(lambda a : a * a, even_list)
# square_even = map(lambda a : a * a , filter(lambda a : a % 2 == 0 ,my_list))
# print(list(square_even),"square_even")

# 17. Sum of Even Numbers

# my_list = [1, 2, 3, 4, 5, 6]

# sum_even = reduce(lambda acc, cuu : acc + cuu, filter(lambda a : a % 2 == 0 ,my_list))
# print(sum_even, "sum_even")

# 18. Count Words with Length Greater Than 3

# my_list = ["cat", "apple", "dog", "banana"]

# result = len(list(filter(lambda a: len(a) > 3, my_list)))
# print(result, "count of word Length Greater Than 3")

# 19. Sum of Squares of Odd Numbers

# my_list = [1, 2, 3, 4, 5]

# odd_list = filter(lambda a: a % 2 != 0, my_list)
# square_list = map(lambda a: a * a, odd_list)
# sum_value = reduce(lambda acc, curr: acc + curr, square_list )

# print(sum_value)

# 20. Sum of Cubes of Even Numbers

my_list = [1, 2, 3, 4, 5, 6]

even_list = filter(lambda a: a % 2 == 0, my_list)
cube_list = map(lambda a: a**3, even_list)
sum_value = reduce(lambda acc, curr: acc + curr, cube_list )

# print(sum_value)