# 4. Anagram Checker

# Practice Problem: Write a function that determines if two strings are anagrams (contain the exact same characters in a different order).

# # version - 1 (using count is inefficient as it check the string again and agian)

word1 = "listen"
word2 = "silent"

def anagram(w1,w2):
    if len(w1) != len(w2):
        return False
    for i in w1:
        if w1.count(i) != w2.count(i):
            return False
    return True 

print(anagram(word1, word2))

# # version - 2 :

word1 = "listen"
word2 = "silent" 

def anagram(w1,w2):
    w1 = w1.lower().replace(" ","")
    w2 = w2.lower().replace(" ","")
    return sorted(w1) == sorted(w2)

print(anagram(word1, word2))

# version - 3 (using Counter)

from collections import Counter

word1 = "listen"
word2 = "silent" 

def anagram(w1,w2):
    w1 = w1.lower().replace(" ","")
    w2 = w2.lower().replace(" ","")
    return Counter(w1) == Counter(w2)

print(anagram(word1, word2))