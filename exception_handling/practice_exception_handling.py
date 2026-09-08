# Exception handling
n = int(input())
try :
    result = 283 / n
except ZeroDivisionError:
    print("Error happened!")
else :
    print(str(result))
finally :
    print("finally is excuting..")

print(type(ValueError))