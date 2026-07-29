my_list = [10,20,30,40,50,60,20]
add_list = [100,200,300,400,500,600,200]
fruit_list = ["apple", "banana", "cherry", "orange",
               "kiwi", "melon", "mango"]


my_list.append("last") 
print(my_list)
my_list.insert(2,"element")
print(my_list)
my_list.extend(add_list)
print(my_list)
print(add_list)
removed_element = my_list.pop(2)
print(my_list)
print(removed_element)
fruit_list.remove("cherry")
print(fruit_list)
splicing = fruit_list[2:5]
print(fruit_list)


