# 13. Bank Account Validation

# Question: Create a BankAccount class with a withdraw() method. Handle negative withdrawal amounts and insufficient balance using exceptions.


# version - 1

class InsufficientBalanceError(Exception):
    pass

class NegativeWithdrawError(Exception):
    pass

class BankAccount:
    def __init__(self, initial_amount):
        self.balance = initial_amount

    def withdraw(self, n):
        try:
            if n <= 0:
                raise NegativeWithdrawError("Withdrawal amount must be positive.")
            if n > self.balance:
                raise InsufficientBalanceError("Insufficient balance")
        except NegativeWithdrawError as e:
            print(f"Error: {e}")
        except InsufficientBalanceError as e:
            print(f"Error: {e}")
        else:
            self.balance -= n
            print("Withdrawal successful")
            print(f"Remaining balance: {self.balance}") 

a = BankAccount(5000)
a.withdraw(4000)


# version - 2 (withdraw() only raises; the caller decides how to handle each error)

class InsufficientBalanceError(Exception):
    pass

class NegativeWithdrawError(Exception):
    pass

class BankAccount:
    def __init__(self, initial_amount):
        self.balance = initial_amount

    def withdraw(self, n):
        if n <= 0:
            raise NegativeWithdrawError("Withdrawal amount must be positive.")
        if n > self.balance:
            raise InsufficientBalanceError("Insufficient balance")
        self.balance -= n

a = BankAccount(5000)

try:
    n = int(input("Withdrawl amount: "))
    a.withdraw(n)
except ValueError:
    print("Error: Enter a valid number")
except NegativeWithdrawError as e:
    print(f"Error: {e}")
except InsufficientBalanceError as e:
    print(f"Error: {e}")
else:
    print("Withdrawal successful")
    print(f"Remaining balance: {a.balance}") 