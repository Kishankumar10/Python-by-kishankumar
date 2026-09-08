# 12. Custom Insufficient Balance Exception

# Question: Create a custom exception called InsufficientBalanceError. Raise it when a user tries to withdraw more money than their balance.

class InsufficientBalanceError(Exception):
    pass

balance = 5000

try:
    n = int(input("Withdrawal amount: "))
    if n <= 0:
        raise ValueError("Invalid request")
    if n > balance:
        raise InsufficientBalanceError("Insufficient balance")
except InsufficientBalanceError as e:
    print(f"Error: {e}")
except ValueError:
    print("Error: Invalid request")
else:
    balance -= n
    print("Withdrawal successful")
    print(f"Remaining balance: {balance}")