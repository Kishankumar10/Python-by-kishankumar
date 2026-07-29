# 11. Write a Python program to find and print
# the index of a specific value in a list.

my_list =["apple", "banana", "orange" , "melon", "mango"]
print(my_list,end="\n\n")
a = input("Give a item form the list : ").strip().lower()
index = 0
for i in my_list :
    if a == i : 
         break
    index += 1
if len(my_list) == index :
    print(f"\n'{a}' is not found in list\n")
else :
    print(f"\nThe index of '{a}' is '{index}'\n")

# print(my_list.index(a))










