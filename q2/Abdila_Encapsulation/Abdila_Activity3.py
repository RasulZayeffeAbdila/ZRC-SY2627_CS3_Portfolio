class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("The Balance must not be a negative number.")
     
    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance

a1 = BankAccount(12345, 1000)

print("Account 1")
print("Account Number:", a1.account_number)
print("Balance: {:.2f}".format(a1.balance))

a1.set_account_number(67010)
a1.set_balance(-100)

print("Account Number:", a1.account_number)
print ("Balance: {:.2f}".format(a1.balance))