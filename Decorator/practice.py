# Decorators practice


def greet():
    return "hello world"

wish = greet     # now both variable name points to same function object


# without calling function you get function's memory address

print(wish) 
print(greet)

# verification 

print(greet())
print(wish())        # both greet and wish will evoke the same function obj

print(id(wish) == id(greet)) # to prove both variable point to same function obj


# since function are merely objects they can be passed as arguments inside other funcion and see the following example

def cap(text):
    return text.upper()

def call(func,value):      # a function can accept another function as input
    return func(value)

result = call(cap,"hello")
print(result)


# now we are clear that a function can accept another function likewise a function can also return another function as a output

def outer():
    def square(x):
        return x * x
    return square     # here the outer function returns  square function 

result = outer()  # result variable receives the 'square function object' so the        
# variable 'result' is binded to the 'square function object'

print(result(5))


### now i combine both the above concepts which are  passing function as a argument and returning a function

def my_decorator(original_function):
    def wrapper():                       
        print("before function runs")
        original_function()
        print("after function runs")
    return wrapper

def say_hi():
    print("hi")

decorated = my_decorator(say_hi)  
# now the decorated recives the wrapper function refernce 


# so now the actually syntax for the decorator

def my_decorator(original_function):
    def wrapper():                       
        print("before function runs")
        original_function()
        print("after function runs")
    return wrapper

def say_hi():
    print("hi")

say_hi = my_decorator(say_hi)  # now the wrapper function is rebinded to the say_hi name

say_hi()   

# say_hi = my_decorator(say_hi)    this line can be done by using decorator syntax @my_decorator


# The final code is written as 


def my_decorator(original_function):
    def wrapper():                       
        print("before function runs")
        original_function()
        print("after function runs")
    return wrapper

@my_decorator
def say_hi():
    print("hi")

say_hi()

# but what if we need to return a value 

def my_decorator(original_function):
    def wrapper(a,b):                 # The name add is rebound to the wrapper function object during @my_decorator       
        print("before function runs")
        value = original_function(a,b)      
        print("after function runs")
        return value    
    return wrapper

@my_decorator
def add(a,b):
    return a + b  

print(add(2,5))  

# but what if we need to use the decorator for different function with different number of parameters
# then we have to use *args to take arg as a tuple and unpack it in the original function call 

def my_decorator(original_function):
    def wrapper(*args,**kwargs):     # args packed into a tuple 
        print("before function runs")           
        value = original_function(*args,**kwargs)    # tuple unpacking 
        print("after function runs")
        return value    
    return wrapper

@my_decorator          
def add(a,b):
    return a + b  

@my_decorator
def add_3(a,b,c):
    return a + b + c 

print(add(2,5)) 
print(add_3(7,9,2))

# If only keyword arguments are passed, *args becomes an empty tuple while **kwargs captures the keyword arguments as a dictionary.