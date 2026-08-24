# Longest word

a = "Python is a amazing language"
largest_word = ""
for i in a.split() :
    if len(i) > len(largest_word)  :
        largest_word = i        
print(largest_word)
