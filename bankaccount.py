# bankaccount.py

class Account():
    """ bank account super class """

    def __init__(self, account_no, balance):
        """ constructor method """
        self.__account_no = account_no
        self.__balance = balance

    def get_account_no(self):
        """ accessor method to retrieve account number """
        return self.__account_no

    def get_balance(self):
        """ accessor method to retrieve balance """
        return self.__balance

##    def set_balance(self, new_balance):
##        """ modifier/mutator method to update balance """
##        self.__balance = new_balance

    def deposit(self, amount):
        """ modifier/mutator method to increase balance """
        self.__balance += amount

    def withdraw(self, amount):
        """ modifier/mutator method to decrease balance """
        self.__balance -= amount

    def display(self):
        """ helper/support method to show account info """
        print("Account No:", self.__account_no)
        print("Balance:", self.__balance)


class SavingsAccount(Account):
    """ savings account subclass """

    def __init__(self, account_no, balance, interest):
        """ subclass constructor method """
        super().__init__(account_no, balance)
        self.__interest = interest

    def calc_interest(self):
        """ helper/support method to compute interest """
        self.deposit(self.get_balance() * (1 + self.__interest))
        # self.__balance # illegal

    def display(self):
        """ helper/support method to show savings account info """
        super().display()
        print("Savings interest:", self.__interest)


class CurrentAccount(Account):
    """ current account subclass """

    def __init__(self, account_no, balance, overdraft):
        """ subclass constructor method """
        super().__init__(account_no, balance)
        self.__overdraft = overdraft

    def withdraw(self, amount): # overrides superclass withdraw
        """ helper/support method to withdraw up to overdraft limit """
        if amount > (self.get_balance() + self.__overdraft): # cannot withdraw more than overdraft limit
            print("Withdrawal amount exceeds overdraft limit.")
        else:
            super().withdraw(amount)
        

    def display(self):
        """ helper/support method to show current account info """
        super().display()
        print("Overdraft limit:", self.__overdraft)
        

# main
savings_acct1 = SavingsAccount("C01", 0, 0.01)
savings_acct1.deposit(500)
savings_acct1.calc_interest()
# savings_acct1.display()

current_acct1 = CurrentAccount("C01", 0, 500)
current_acct1.withdraw(300)
current_acct1.withdraw(300)
# current_acct1.display()

accounts = []
accounts.append(savings_acct1)
accounts.append(current_acct1)
for account in accounts:
    account.display()
