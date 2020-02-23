# 12 lines: Classes
class BankAccount(object):

    def __init__(self, initial_balance=0, id_number=1111):
        self.balance = initial_balance
        self.id_number = id_number

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def overdraw(self):
        return self.balance < 0


my_account = BankAccount(15, 2000)
my_account.withdraw(50)
print(my_account.id_number, my_account.balance, my_account.overdraw())
