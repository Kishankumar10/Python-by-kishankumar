# 3. Frequency Map with Counter

# Practice Problem: Create a function that takes a string and returns a count
#  of how many times each character appears. Ignore spaces and make it
#  case-insensitive.

from collections import Counter
text = "Python Programming"

def character_frequency(string):
    filtered_string = string.replace(" ","").lower()
    return Counter(filtered_string)

print(character_frequency(text))