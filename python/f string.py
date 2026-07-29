####f string 
##
##Task 1 ⭐ (Warm-up)
##
##Ask the user for:
##
##Name
##Age
##
##Output:
##
##Hello Alex!
##You are 18 years old.
##
##Use only one print().

a=input("What is your name          :")
b=input("What is your account no.   :")
c=float(input("What is your old balance   :"))
d=float(input("What is your deposit amount:"))
print("==============================")
print()
print("BANK RECEIPT".center(30))
print()
print("==============================")
print()
print(f"Customer Name : {a}")
print(f"Account No.   : {b}")
print()
print(f"Old Balance   : ₹{c:.2f}")
print(f"Deposit       : ₹{d:.2f}")
print()
print(f"New Balance   : ₹{c+d:.2f}")
print()
print("Thank you for banking with us.")
print("==============================")
