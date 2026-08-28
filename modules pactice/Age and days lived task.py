from datetime import date,datetime

# # version - 1

# DOB_string = input("Enter your date of birth (format: dd/mm/yyyy ) : ")
# today = datetime.now()

# DOB = datetime.strptime(DOB_string,"%d/%m/%Y")

# diff = today - DOB

# days_lived = diff.days
# age = days_lived/365.25

# print(f"Your age is : {int(age)}")
# print(f"You have lived for {days_lived} days uselessly")

# version - 2

DOB_string = input("Enter your date of birth (format: dd/mm/yyyy ) : ")
today = date.today()

DOB = date.strptime(DOB_string,"%d/%m/%Y")
diff = today - DOB
days_lived = diff.days
age = today.year - DOB.year

# if the current month is not greater than the birth month then the year_diff
# must be subtracted by one and the same logic is also required for date 

if DOB.month > today.month :
    age -= 1
elif DOB.month == today.month and DOB.day > today.day:
    age -= 1
    
print(f"Your age is : {age}")
print(f"You have lived for {days_lived} days")