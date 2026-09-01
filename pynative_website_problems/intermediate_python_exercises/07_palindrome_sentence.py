# 7. Palindrome Sentence

# Practice Problem: Write a function to check if a full sentence is a palindrome. You must ignore case, spaces, and all punctuation marks.

# version - 1 :

sentence = "A man, a plan, a canal: Panama"

def palindrome_sentence(string):
    cleaned_data = ""
    for i in string:
        if i.isalnum():
            cleaned_data += i.lower() 
    for i in range(len(cleaned_data)//2):
        if cleaned_data[i] != cleaned_data[-i-1]:
            return False
    return True

print(palindrome_sentence(sentence))

# version - 2 (using generators)

sentence = "A man, a plan, a canal: Panama"

def palindrome_sentence(string):
    cleaned_data = "".join(char.lower() for char in string if char.isalnum())
    for i in range(len(cleaned_data)//2):
        if cleaned_data[i] != cleaned_data[-i-1]:
            return False
    return True

print(palindrome_sentence(sentence))