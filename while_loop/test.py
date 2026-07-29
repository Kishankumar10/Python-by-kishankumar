# print("****","****","****","****",sep="/n")
#  print("****/n****/n****/n****")
# a = "after"
# print(f"{s} world")
# a = "hi i am  good and fine "
# b = a.split()
# c = a.split(" ")
# d = a.split("  ")
# print(b)
# print(c)
# print(d)
# numbers = ["10", "20", "30"]
# result = map(int, numbers)
# print(result)
# X,Y = map(int,input().split())
# print(X*Y)
# a = map(int,"1 8 5 0 8 38".split())
# print(list(a))
# print(a)
# words = ["apple", "banana"]
# print(list(map(str.upper, words)))
# cook your dish here
# a = input()
# v = "aeiou"
# result = 0
# i = 0
# while i < len(a):
#     if a[i] in v :
#         result += 1 
#     i += 1
# print(result)


# 🛠️ Phase 1 Graduation ChallengeTry to build a Simple Guessing Game 
# without looking at old code:
# The program picks a secret number between 1 and 20.
# It uses a while loop to give the user 5 chances to guess.
# It uses if/elif/else to say "too high", "too low", or "you win!".

# import random
# a = random.randint(1, 10)
# i = 0 
# while i < 5:
#     i +=1
#     guess = int(input("Guess a number between 1 to 10 : "))
#     if guess == a :
#         print("You Win!")
#         break
#     elif guess > a:
#         print("Too high")
#     elif guess < a:
#         print("Too low")
# if guess != a:
#     print(f"Game Over! The number was {a}.")

# Player 1 sets the secret target number
# a = int(input("Player 1, enter a secret number (1 to 10): "))

# Print 50 blank lines to hide the answer from Player 2's sight!
# print("\n" * 50)

# print("Player 2, it's your turn to guess!")

# --- THE REST OF YOUR GAME LOGIC ---
# i = 0 
# while i < 5:
#     i += 1
#     guess = int(input("Guess a number between 1 to 10 : "))
#     if guess == a:
#         print("You Win!")
#         break
#     elif guess > a:
#         print("Too high")
#     elif guess < a:
#         print("Too low")

# if guess != a:
#     print(f"Game Over! The number was {a}.")
# word = ["hi"]
# for x in word:
#     for y in x:
#         print(y)
# a = [5,6,7,8,9]
# print(a[-435])
# numbers = [1,2]
# numbers = numbers.append(3)
# print(numbers)
# a = "HI"
# a = a.upper()
# print(a)
# a = []
# a.append("Python")
# a.append(["Java", "C"])
# a.append(100)
# print(a[1][0])

# a = [10, 20, 30]
# a.insert(-100, 99)
# print(a)

# a = [1, 2, 3, 2, 4]
# a.remove(2)
# print(a)

# a = [1,2,3]
# a.remove(5)
# print(a)

# a = [1,2,3]
# x = a.clear()
# print(a)
# print(x)
x = 42

match x:
    case number:
        print(number)
print(x)
