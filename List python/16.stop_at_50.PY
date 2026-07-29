# 16. Write a Python program to print list elements 
# until the number 50 appears (stop when found).

# VERSION - 1

my_list = [12,23,45,61,50,84,12,18,1,20]
final_list = []
for i in my_list :
    if i == 50 :
        break
    final_list.append(i)
print("\n",final_list,"\n")        


# VERSION - 2

# final_list = my_list[:my_list.index(50)]
# print("\n",final_list,"\n")















