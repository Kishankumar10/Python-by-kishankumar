# Encapsulation

# 1. Public Access

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Alice")

print(s1.name)  # the object's attribute is publicly accessible
s1.name = "Bob"  # now the s1 instance's attribute has been modified
print(s1.name)



# 2. Protected Access

class Mark:
    def __init__(self, mark):
        self._mark = mark

class Result(Mark):
    def print_result(self):
        print(self._mark)

# _mark is just a naming convention, meaning this instance attribute is meant to be used only inside the class and its subclasses, not accessed publicly

m1 = Result(85)
m1.print_result()

# but it is not fully protected; it can still be accessed and modified using the name _mark
m1._mark = -10000
print(m1._mark)



# 3. Private Access

class Employee:
    def __init__(self, name, password):
        self.name = name
        self.__password = password

a = Employee("Jackson Storm", 911)

print(a.name)
# print(a.__password)   (throws an error)

# so we cannot access the attribute __password directly
# because Python does name mangling and converts the name __password to _Employee__password, then stores it under that name

# but it is still accessible if we use the mangled attribute name
print(a._Employee__password)

# so Python's encapsulation is meant to avoid accidental name overrides, not for security


# 4. Property Decorators (Getters and Setters)

class Student:
    def __init__(self, name, mark):
        self.name = name
        self.__mark = mark  # storing mark as a private attribute

    # @property works as a getter method
    # so we can access __mark like a normal attribute using obj.mark without calling a function like obj.get_mark()
    @property
    def mark(self):
        return self.__mark

    # @mark.setter works as a setter method
    # so when we assign a value like obj.mark = 55, this setter automatically runs and validates the value before updating
    @mark.setter
    def mark(self, new_mark):
        if 0 <= new_mark <= 100:
            self.__mark = new_mark  
        else:
            print("Invalid mark! mark must be between 0 and 100")

# testing getter and setter
obj = Student("Kishankumar", 100)
print(obj.__dict__)
print(obj.mark) # access the private variable using simple attributes access

obj.mark = 55  # calls @mark.setter to validate and update __mark
print(obj.mark)

obj.mark = -23  # fails validation in @mark.setter, so __mark stays unchanged


# Flaw: Bad initial data sneaks through because setter was never called
bad_student = Student("Badboss", -999)
print(bad_student.mark)  # Output: -999 (Invalid data saved in memory!)


# Fix: __init__ now writes self.mark (the property name), NOT self.__mark directly.
# Since "mark" is intercepted by the property descriptor, this assignment is
# ALWAYS redirected to the setter — even during construction — so the same
# 0-100 validation applies to the very first value, not just later updates.

class Student:
    def __init__(self, name, mark):
        print('STEP A: about to run self.mark = mark')
        self.name = name
        self.mark = mark
        print('STEP E: init is done')

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, new_mark):
        print(f'STEP B: setter called with new_mark = {new_mark}')
        if 0 <= new_mark <= 100:
            print('STEP C: valid, about to run self.__mark = new_mark')
            self.__mark = new_mark
            print('STEP D: self._Student__mark now exists in instance dict')
        else:
            self.__mark = 0

s = Student('Kishankuamr', 85)
print(s.__dict__)