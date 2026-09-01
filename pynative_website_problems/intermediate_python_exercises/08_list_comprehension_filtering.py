# 8. List Comprehension Filtering (Advanced)

# Practice Problem: Given a list of strings, use a single list comprehension to extract strings that meet two criteria: they must be longer than 5 characters AND they must start with a vowel (a, e, i, o, u).


my_list = ["apple", "education", "ice", "ocean", "python", "umbrella"]

def filter_long_vowel_strings(str_lst):
    return [i for i in str_lst if len(i)>5 and i[0].lower() in "aeiou"]

print(filter_long_vowel_strings(my_list))
