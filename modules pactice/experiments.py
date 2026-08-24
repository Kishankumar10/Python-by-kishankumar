# class studentData :
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     def total(self):
#         result = 0
#         for i in self.marks :
#             result += i
#         return result

# student_1 = studentData('gemini',[90, 95, 99, 100, 91])

# print(student_1.name)
# print(student_1.total())

# Exercise 1: The Basic Blueprint (Book)
# Build a simple class to store information about a book.

# Class Name: Book

# Attributes (__init__): title, author, pages

# Method: summary(self) — prints a string like: "'1984' by George Orwell (328 pages)".

# Goal: Get comfortable using self to assign and read basic instance variables.


# class Book :
#     def __init__(self,title,author,pages):
#         self.title = title
#         self.author = author
#         self.pages = pages 
#     def is_long(self):
#         return self.pages > 300

# b1 = Book("Dune", "Frank Herbert", 412)
# print(b1.title) 
# print(b1.author) 
# print(b1.pages) 
# print(b1.is_long())
# print(b1.__dict__)

# import datetime
# for i in datetime.__dict__:
#     print(i)

# n = int(input("how many items you want : "))

# first = 0
# second = 1

# fab_list = [first, second]
# for i in range(n-2):
#     third = first + second 
#     fab_list.append(third)
#     first = second 
#     second = third
    
# print(fab_list)

def double_char(string):
  return ''.join(map(lambda a : a*2, string))

print(double_char("The"))