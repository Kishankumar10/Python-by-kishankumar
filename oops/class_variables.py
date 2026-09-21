class TestClass:
    number_of_student = 0
    mark_increase = 10

    def __init__(self, name, mark, email):
        self.name = name
        self.mark = mark
        self.email = email
        TestClass.number_of_student += 1

    def extra_marks(self):
        self.mark += self.mark_increase


person_1 = TestClass("aaa", 95, "aaa.pdy@gmail.com")
person_2 = TestClass("bbb", 0, "bbb.pdy@gmail.com")


# 1. Inspecting basic instance attributes
print("Name:", person_1.name)
print("Mark:", person_1.mark)
print("Email:", person_1.email)


# 2. Modifying class variable for everyone
TestClass.mark_increase = 5000
person_1.extra_marks()
print("Mark after increase:", person_1.mark)


# 3. Checking dictionary before adding local variable
print("person_1 dict before:", person_1.__dict__)

# Creating instance override (shadowing)
person_1.mark_increase = 6000

# Checking dictionary after adding local variable
print("person_1 dict after:", person_1.__dict__)

# Comparing values across class and instances
print("TestClass mark increase:", TestClass.mark_increase)
print("person_1 mark increase:", person_1.mark_increase)
print("person_2 mark increase:", person_2.mark_increase)

# Checking total count
print("Total students:", TestClass.number_of_student)