# Reading a file 

file = open("text_file_1.txt","r")
data = file.read()
print(data)
file.close()

# reading line by line 

file = open("text_file_1.txt","r")
data_1 = file.readline()
data_2 = file.readline()
data_3 = file.readline()
data_4 = file.readline()
print(data_1)
print(data_2)
print(data_3)
print(data_4)
file.close()

# storing the each lines as a seperate string in the list 

file = open("text_file_1.txt","r")
data = file.readlines()
print(data)
file.close()

# writing new data in already existent file 

file = open("text_file_1.txt","w")
new_content = "The old content are deleted\nThe new content is written\n"
extra_content = "seperate write() method is used again"
file.write(new_content)
file.write(extra_content)
file.close()

# using write mode to create a new file by giving a new file name

file = open("text_file_creation.txt","w")
new_content = "A new file is created using the write mode\n"
file.write(new_content)
file.close()


# appending the date to the created text file 

file = open("text_file_creation.txt","a")
appending_content = "now i am appending a new data"
file.write(appending_content)
file.close()

# using appending mode to create a new file 

file = open("text_file_creation_2.txt","a")
appending_content = "now i am appending a new data to a new file"
file.write(appending_content)
file.close()

# creating a file exclusively if the file name is already present then it raises an error

file = open("text_exclusive_file.txt","x")
new_content = "now i am writing new data in the new file by x mode"
file.write(new_content)
file.close()

# using the os modult to rename a file, remove a file and create a directory 

import os 

os.rename("test_file.txt", "demo_file.txt")
os.remove("demo_file.txt")
os.mkdir("new folder created")


# file = open("text_file_1.txt", "r")

# data_1 = file.read()
# data_2 = file.read()

# print("First read:", data_1)
# print("Second read:", data_2)

# file.close()