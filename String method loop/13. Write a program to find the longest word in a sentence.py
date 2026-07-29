a = input("Enter your sentence : ")
current_word = ""
longest_word= ""

for i in a:
    if i != " " :
        current_word += i
    else :
        if len(longest_word) < len(current_word):
            longest_word = current_word
        current_word = ""

if len(current_word)>len(longest_word):
    longest_word = current_word

print(f"'{longest_word}' is the longest word")
