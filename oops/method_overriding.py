# Base class Animal

class Animal:
    def speak(self):
        return "Some generic sound"

# Dog inherits from Animal
class Dog(Animal):
    def speak(self):  # override the parent method 
        return "Bark"

d1 = Dog()
print(d1.speak())

# How to access the base class speak method 
class Cat(Animal):
    def speak(self):
        return f"{Animal.speak(self)} followed by Meow"
# Animal.speak(self), we are calling the Animal class method so we have to pass the object memory refernce 

c1 = Cat()
print(c1.speak())


# Python provides a function super() for this approx behaviour
class NewlyFoundAnimal(Animal):
    def speak(self):
        return f"Unknown: {super().speak()}"
    
alien = NewlyFoundAnimal()  
print(alien.speak())

# Unlike Animal.speak(self) which is hardcoded, super() follows MRO (Method Resolution Order) to find the speak method 