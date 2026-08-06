# task 

studentsData = [
    {
        "name":"aaa",
        "email":"aaa@gmail.com",
        "mobile":3894723893,
        "address": "No:1, aa str",
        "marks":[70,99,77,89,67]
    },
    {
          "name":"bbb",
          "email":"bbb@gmail.com",
          "mobile":938573534,
          "address": "No:1, bbb str",
          "marks":[100,99,97,90,98]
    },
    {
           "name":"ccc",
           "email":"ccc@gmail.com",
           "mobile":327647335,
           "address": "No:1, cc str",
           "marks":[56,90,48,89,95]
    },
]

# find the total marks of first student
# total = 0 
# for i in studentsData[0]["marks"] :
#      total += i 
# print("find the total marks of only first student")
# print(total)  

# if the total is asked for every student the 
for student in studentsData :
     total = 0 
     for mark in student["marks"] :
         total += mark
     print(f"student '{student["name"]}' had scored {total} marks")