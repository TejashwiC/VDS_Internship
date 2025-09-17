class BankAccount:
    def __init__(self,account_number,account_holder,balance=0):
        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"deposited {amount}.new balance={self.balance}")
        else:
            print("deposit amount must be positive")
    def withdraw(self,amount):
        if amount>self.balance:
            print("insuffienct balance")

        elif amount<=0:
            print("withdrawl amount must be positive")
        else:
            self.balance-=amount
            print(f"withdrawal{amount}.new balance={self.balance}")
    def check_balance(self):
        print(f"Current Balance for {self.account_holder}: {self.balance}")

    def account_info(self):
        print("Account Information")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")

acc1 = BankAccount(1000, "Teja", 5000)

acc1.account_info()

acc1.deposit(2000)

acc1.withdraw(0)

acc1.check_balance()
    
