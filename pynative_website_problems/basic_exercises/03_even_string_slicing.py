# 3. String Indexing and Even Slicing

# Practice Problem: Display only those characters which are present at an even index number in given string.

my_string = "pynative"

def display_even_chr(string):
    for i in range(0, len(string), 2):
        print(string[i])

display_even_chr(my_string)

# for slicing practice 

print(my_string[::2])