# 2. Create a set of unique words from a sentence, where words are
# separated by spaces and punctuation marks should be ignored.

sentence = "That is all I want, all I need."
unique_set = set()
words_list = sentence.split()

for word in words_list:
    word = word.strip(".,?!:;")
    unique_set.add(word)

print(unique_set)