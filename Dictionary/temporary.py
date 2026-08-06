# # key value pair
# #  ordered
# # mutable

# studentInfo = {
#     "name":"aaa",
#     "regNo": 1001,
#     "mobile":948357439,
#     "isPass": True
# }
# # print(type(studentInfo))

# # dict2 = dict(courseName = "python", duration = 3)
# # print(dict2)

# # # access
# print(studentInfo["regNo"])
# print(studentInfo.get("regNo"))

# # # modify
# # studentInfo["total"] = 460
# # print(studentInfo,"after modify")

# # studentInfo["mobile"] = 9488301956
# # print(studentInfo,"after modify")

# # # remove

# # del studentInfo["isPass"]
# # print(studentInfo,"after del")

# # print(dict2.pop("duration"))
# # # print(dict2.pop("fee"))

# # # looping items(), values, keys()

# # for i in studentInfo.keys():
# #     print(i,"keys")

# # for i in studentInfo.values():
# #     print(i,"values")

# # for x,y in studentInfo.items():
# #     print(x , y)


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

# # for i in studentsData:
# #     print(i,"students")
a = [1,2,3,4,5,6]
total = 0
for i in a :
    total += i
print(total)