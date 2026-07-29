## Check Whether a Person is a Child, Teen, Adult, or Senior

##Child: 0–12 years
##Teen: 13–19 years
##Adult: 20–59 years
##Senior: 60 years and above

age=int(input("what is your age:"))

if   age < 0 :
    print("age cannot be negative")
elif age < 13:
    print("you are a child")
elif age < 20:
    print("you are a teenager")
elif age < 60:
    print("you are an adult")
else:
    print("you are a senior citizen ")
