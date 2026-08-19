# Function practice

def function():
    print("function is successfully called")

function()

# addition function 

def adder(x,y):
    print(x + y)

test_case = int(input("How many additions you want to perform : "))

for i in range(test_case):
    a = int(input("First number : "))
    b = int(input("Second number : "))
    adder(a,b)


# local scope

def printer():
    x = 600
    print(x,"local variables")
printer()

# global scope

z = 657

def function_1():
    print(z,"global variable")

function_1()

# enclosed scope

def outer():
    h = 15
    def inner():
        print(h,"variable found enclosed scope")
    inner()
outer()

# global keyword

g = 1000
def outer():
    g = 100
    def inner():
        global g
        g = 10
        print(g , "inner variable")
    inner()
    print(g , "outer variable")
outer()
print(g,"global variable")

# non local keyword

g = 1000
def outer():
    g = 100
    def inner():
        nonlocal g
        g = 10
        print(g , "inner variable")
    inner()
    print(g , "outer variable")
outer()
print(g,"global variable")
