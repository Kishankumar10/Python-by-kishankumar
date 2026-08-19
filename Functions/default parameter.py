# Return

def add_1(a,b):
    return a+b

result = add_1(12,4)
print(result)

# default parameter

def add_2(a,b=0,c=0):
    return a+b+c

print(add_2(3),"with only one argument")
print(add_2(12,3,1),"with all argument")

# Arbitrary Positional Arguments

def total(*num):
    result = 0 
    for i in num :
        result += i 
    return result
     
T = total(1,5,6,3,2,4)
print(T)

def fun_1(a,b,*leftover):
    print(a)
    print(b)
    print(leftover)

fun_1(1,5,6,3,2,4)

# Arbitrary Keyword Arguments 

def fun_2(**info):
    for i in info.items():
        a,b = i 
        print(f"keys : {a} , values : {b}")

fun_2(name = "Kishankumar",course = "python",days = 36)


