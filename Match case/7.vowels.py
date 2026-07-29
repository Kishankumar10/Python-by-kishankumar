# 7. Write a program to check whether a character
# is a *vowel or consonant* using match.
character = input("Enter a alphabet character : ")
match character.lower() :
    case a if len(a)!=1 :
        print("Enter a single character")
    case a if not (a.isalpha()) :
        print("Enter a valid alphabet character")
    case "a"|"e"|"i"|"o"|"u" :
        print("The given character is a vowel")
    case _ :
        print("The given character is a consonant") 

