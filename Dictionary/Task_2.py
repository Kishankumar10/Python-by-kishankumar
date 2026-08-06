# Task - 2

studentsData = [
    {
        "name":"aaa",
        "email":"aaa@gmail.com",
        "mobile":3894723893,
        "marks":[70,99,77,89,67]
    },
    {
        "name":"bbb",
        "email":"bbb@gmail.com",
        "mobile":938573534,
        "marks":[100,99,97,90,98]
    },
    {
        "name":"ccc",
        "email":"ccc@gmail.com",
        "mobile":327647335,
        "marks":[56,90,48,89,95]
    },
]

# Version - 1


for i in studentsData :              # adding total to the dict of list
     total = 0 
     for j in i["marks"] :  
         total += j
     i["total"] = total

a = []                               # creating a empty list and appending total marks
for i in studentsData:
    a.append(i["total"])
a.sort()                             # sorting the list and reversing it
a = a[::-1]

for i in studentsData :
    rank = a.index(i["total"]) + 1    # considering the index position as rank
    i["rank"] = rank                   

for i in studentsData :             # adding feedback to dict by conditional statement
    if i["total"] > 450 :
        i["feedback"] = "Very good"
    elif i["total"] > 400:
        i["feedback"] = "good"
    else :
        i["feedback"] = "need improvement"

print(studentsData)

# ______________________________________________________________________________________#


















































# For more clearer dictionary visualization

# for i in studentsData :
#     print("\n",i,"\n")