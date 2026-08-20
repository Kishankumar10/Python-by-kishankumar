# module - 1 

studentsData = [
        {
        "name": "aaa",
        "email": "aaa@gmail.com",
        "mobile": 3894723893,
        "marks": [95, 99, 100, 90, 100]
    },
    {
        "name": "bbb",
        "email": "bbb@gmail.com",
        "mobile": 938573534,
        "marks": [24, 21, 26, 50, 48]
    },
    {
        "name": "ccc",
        "email": "ccc@gmail.com",
        "mobile": 327647335,
        "marks": [78, 100, 60, 56, 75]
    },
]

def average(mark_list):
    total_of_marks = sum(mark_list)
    no_of_marks = len(mark_list)
    avg_value = total_of_marks / no_of_marks
    return avg_value

def total(mark_list):
    acc = 0
    for i in mark_list:
        acc += i
    return acc

def grade(mark_list):
    total_mark = total(mark_list)
    if total_mark >= 400:
        return "A"
    if total_mark >= 300:
        return "B"
    if total_mark >= 175:
        return "C"
    return "D"  

def ispass(mark_list):
    result = "Pass"
    for i in mark_list:
        if i < 35 :
            result = "Fail"
            break
    return result

def feedback(mark_list):
    total_mark = total(mark_list)
    if total_mark >= 400:
        return "Excellent"
    if total_mark >= 300:
        return "Good"
    if total_mark >= 175:
        return "Need improvement"
    return "Must work hard" 