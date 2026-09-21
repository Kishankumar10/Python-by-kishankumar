from abc import ABC, abstractmethod

# Inheriting from ABC makes Animal an abstract base class (template)
class Animal(ABC):
    @abstractmethod
    def sound(self):  # No code here, just setting the rule!
        pass


# Valid child class
class Dog(Animal):
    def sound(self):  # Fulfills the requirement
        return "Dog barks"


# Incomplete child class
# Because sound() is not defined here, Cat inherits the un-implemented abstract method
# This causes Cat to remain abstract as well
class Cat(Animal):  
    def sleep(self):
        return "silently spleeping"


d = Dog()
print(d.sound())  # Output: Dog barks

# c = Cat()  # Throws error: TypeError as Cat is still abstract
