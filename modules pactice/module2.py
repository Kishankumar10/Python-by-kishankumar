# module-2

from module1 import total
import module1 as m1

def result_printer(list_of_dict):
    for stu_dict in list_of_dict:
        marks = stu_dict["marks"]
        result_dict = {
            "Name" : stu_dict["name"],
            "Marks" : marks,
            "Total" : total(marks),
            "Percentage" : m1.average(marks),
            "Grade" : m1.grade(marks),
            "Result" : m1.ispass(marks),
            "Feedback" : m1.feedback(marks)
        }

        for i,j in result_dict.items() :
            print(f"{i} : {j}")
        print("-"*20)


result_printer(m1.studentsData)



