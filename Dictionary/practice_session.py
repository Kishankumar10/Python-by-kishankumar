# Dictionary

student_info = {
    "name" : "Kishankumar",
    "roll_number" : 123456 ,
    "mobile" : 1234567890 ,
    "ispass" : True ,
    "course" : "python",
    "marks" : [93, 85, 95, 98, 96, 88]
    }
print(type(student_info))

# accessing

print(student_info["course"])

print(student_info.get("mobile", "Not Found"))
print(student_info.get("speed", "Not Found"))

# modifying and adding new key value pairs

student_info["course"] = "rust"
student_info["learning pace"] = "very slow"
print(student_info, "after modifying and adding")

# remove

del student_info["ispass"]
print(student_info, "after removing")

print(student_info.pop("mobile", "no mobile number"))
print(student_info.pop("ispass", "not specified"))

# loop over keys
# by default loop over 
for i in student_info.keys() :
    print(i,"keys",sep = "-")
for i in student_info :
    print(i,"keys",sep = "-")

# loop over values 

for i in student_info.values() :
    print(i,"values",sep = "-")

# loop over items 

for a,b in student_info.items() :
    print(a, b, sep = "-")

a = dict(i = "hi" , j = "hello")
print(a)