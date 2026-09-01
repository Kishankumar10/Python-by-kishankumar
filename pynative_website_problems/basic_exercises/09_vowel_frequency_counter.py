# 9. Vowel Frequency Counter

# Practice Problem: Write a program to count the total number of vowels (a, e, i, o, u) present in a given sentence.

sentence = "Learning Python is fun!"
vowels = "aeiou"
counter = 0 
for char in sentence.lower():
    if char in vowels:
        counter += 1
print(counter) 
