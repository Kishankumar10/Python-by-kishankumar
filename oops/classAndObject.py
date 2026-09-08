# Class and object

class A:
    inst = "inst data"

var = A()
print(var.inst)

class B:
    inst = "data"
    def func(self):
        print("Function is working")

var = B()
var.func()

class C:
    inst = "data"

    def __init__(self, name, age, language):
        self.UserName = name
        self.age = age
        self.language = language

    def next_year(self):
        return self.age + 1

obj = C("Boss", 17, "Python")
print(obj.inst)
print(obj.UserName)
print(obj.age)
print(obj.language)
print(obj.next_year())