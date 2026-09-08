# Single inheritance

class Parent:
    def func_1(self):
        print("Parent method is working")

class child(Parent):
    def func_2(self):
        print("child method is working")

obj = child()            # only created obj using child class
obj.func_2()      # we can access the method in child class
obj.func_1()      # we can access the method in parent class 



# Multilevel Inheritance

class grandfather:
    def func_1(self):
        print("Grandfather method is working")

class father(grandfather):
    def func_2(self):
        print("father method is working")

class child(father):
    def func_3(self):
        print("child method is working")

obj = child()       # only created obj using child class
obj.func_3()        # we can access the method in child class
obj.func_2()        # we can access the method in father class
obj.func_1()        # we can access the method in grandfather class



# Multiple Inheritance

class father:
    def func_1(self):
        print("father method is working")

class mother:
    def func_2(self):
        print("mother method is working")

class child(father, mother):
    def func_3(self):
        print("child method is working")

obj = child()   # only created obj using child class
obj.func_3()    # we can access the child method
obj.func_2()    # we can access the mother method
obj.func_1()    # we can access the father method

# mother class can't access the father methods



# Hierarchical Inheritance

class Master:
    def func_master(self):
        print("Master method is working")

class child_1(Master):
    def func_1(self):
        print("child_1 method is working")
        
class child_2(Master):
    def func_2(self):
        print("child_2 method is working")

class child_3(Master):
    def func_3(self):
        print("child_3 method is working")

obj = child_1()   
obj.func_master()   # we can access the Master method
obj.func_1()        # we can access the child_1 method

obj = child_2()   
obj.func_master()   # we can access the Master method
obj.func_2()        # we can access the child_2 method

obj = child_3()   
obj.func_master()   # we can access the Master method
obj.func_3()        # we can access the child_3 method