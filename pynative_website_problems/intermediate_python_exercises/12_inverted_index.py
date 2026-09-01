# 12. Inverted Index

# Practice Problem: Create a function that “inverts” a dictionary. Convert a dictionary of Author: [List of Books] into a dictionary of Book: Author.

# version - 1 :

my_dict = {
    "Orwell": ["1984", "Animal Farm"], 
    "Huxley": ["Brave New World"]
    }

def create_inverted_index(ori_dict):
    inverted = {}
    for key,value in ori_dict.items():
        for book in value:
            inverted[book] = key
    return inverted

print(create_inverted_index(my_dict))

# another version (same algorithum but with dict comprehension)

my_dict = {
    "Orwell": ["1984", "Animal Farm"], 
    "Huxley": ["Brave New World"]
    }
def create_inverted_index(ori_dict):
    return {
        book : author                
        for author, books in ori_dict.items()
        for book in books
    }
print(create_inverted_index(my_dict))