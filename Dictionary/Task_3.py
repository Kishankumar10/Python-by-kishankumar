# sorting by rank based 
studentsData = [
    {
        "name": "aaa",
        "email": "aaa@gmail.com",
        "mobile": 3894723893,
        "marks": [55, 99, 53, 90, 67]
    },
    {
        "name": "bbb",
        "email": "bbb@gmail.com",
        "mobile": 938573534,
        "marks": [54, 51, 46, 100, 88]
    },
    {
        "name": "ccc",
        "email": "ccc@gmail.com",
        "mobile": 327647335,
        "marks": [78, 100, 60, 56, 75]
    },
    {
        "name": "ddd",
        "email": "ddd@gmail.com",
        "mobile": 327647335,
        "marks": [45, 95, 75, 97, 82]
    },
    {
        "name": "eee",
        "email": "eee@gmail.com",
        "mobile": 327647335,
        "marks": [53, 61, 84, 90, 71]
    },
    {
        "name": "fff",
        "email": "fff@gmail.com",
        "mobile": 327647335,
        "marks": [50, 98, 45, 58, 69]
    },
    {
        "name": "ggg",
        "email": "ggg@ggg.com",
        "mobile": 327647335,
        "marks": [80, 99, 64, 78, 97]
    },
    {
        "name": "hhh",
        "email": "hhh@gmail.com",
        "mobile": 327647335,
        "marks": [77, 100, 90, 93, 100]
    },
    {
        "name": "iii",
        "email": "iii@gmail.com",
        "mobile": 327647335,
        "marks": [49, 95, 80, 50, 60]
    },
    {
        "name": "jjj",
        "email": "jjj@gmail.com",
        "mobile": 327647335,
        "marks": [80, 59, 93, 42, 55]
    }
]

result = []
total_list = []

for i in studentsData :
    total = sum(i["marks"])
    total_list.append(total)
sorted_list = sorted(total_list,reverse = True)

for i in sorted_list :
    position = total_list.index(i)
    d = studentsData[position]
    result.append({
        "name" : d["name"],
        "email" : d["email"],
        "mobile" : d["mobile"],
        "marks" : d["marks"],
        "total" : i,
        "rank" : sorted_list.index(i) + 1 
    })
for i in result :             
    if i["total"] > 450 :
        i["feedback"] = "Very good"
    elif i["total"] > 400:
        i["feedback"] = "good"
    else :
        i["feedback"] = "need improvement"

print(result)

# for more clear dictionary
#  visulaization 
# for i in result :
#     print("\n",i,"\n")

#________________________________________________
# version - 2 (for duplicates)

result = []
for i in studentsData :
    result.append({
        "name" : i["name"],
        "email" : i["email"],
        "mobile" : i["mobile"],
        "marks" : i["marks"],
        "total" : sum(i["marks"]),
    })

