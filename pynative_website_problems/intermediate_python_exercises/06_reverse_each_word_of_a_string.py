# 6. Reverse Each Word of a String

# Practice Problem: Given a sentence, reverse each individual word within the string while maintaining the original word order.

sentence = "Python is awesome"

def reverse_words(string):
    words_list = string.split()
    return " ".join([i[::-1] for i in words_list])

print(reverse_words(sentence))