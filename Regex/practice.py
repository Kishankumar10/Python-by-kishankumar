import re

my_string = "train is running while its raining in spain"
pattern = re.findall("ai",my_string)
print(pattern)

my_string = "The rain in Spain"
x = re.search(r"\s", my_string) 
print(x.start())
print(x.end())

my_string = "Python is slower than c++"
result = re.split(r"\s", my_string)
print(result)

my_string = "hellopython  world"
result = re.split(r"\s", my_string)
print(result)

my_string = "I am a python student"
result = re.split(r"\s", my_string, maxsplit=2)
print(result)

my_string = "Decorators-are-hard"
result = re.sub("-"," ", my_string)
print(result)