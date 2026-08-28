#  1: List Comprehension Mastery

# Practice Problem: Write a single-line list comprehension that takes a list of strings, filters out strings shorter than 4 characters, and converts the remaining strings to uppercase.

# my version :

words = ["apple", "bat", "cherry", "dog", "elderberry"]

def len4_upper(str_list):
    len_filter = map(lambda a : a.upper(),filter(lambda a : len(a) >= 4, str_list ))
    return list(len_filter)

print(len4_upper(words))

# list Comprehension verison 

words = ["apple", "bat", "cherry", "dog", "elderberry"]

def len4_upper(str_list):
    filtered_list = [i.upper() for i in str_list if len(i) >= 4 ]
    return filtered_list

print(len4_upper(words))