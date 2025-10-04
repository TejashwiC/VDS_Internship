class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance = {self.balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance = {self.balance}")

    def check_balance(self):
        print(f"Current Balance for {self.account_holder}: {self.balance}")

    def account_info(self):
        print("Account Information")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")
acc1 = BankAccount("Teja", 5000)
acc2 = BankAccount("Poojitha", 6000)
acc1.account_info()
acc1.deposit(2000)
acc1.withdraw(0)   
acc1.check_balance()
acc2.account_info()
acc2.deposit(1000)
acc2.withdraw(300)
acc2.check_balance()
