class BankAccount:
    # variable
    accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        # need to append to link instances to variable 
        BankAccount.accounts.append(self)


# 1 - deposit(self, amount) - 
# increases the account balance by the given amount

    def deposit(self, amount):
        self.balance += amount
        return self
# 2 - withdraw(self, amount) - 
# decreases the account balance by the given amount if there are sufficient funds; 
# if there is not enough money, 
# print a message "Insufficient funds: Charging a $5 fee" and deduct $5

    def withdraw(self,amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print ("Insuffient Funds: Charging a $5 fee")
            self.balance -= 5
        return self
# 3 - display_account_info(self) - 
# print to the console: eg. "Balance: $100"
    def display_account_balance(self):
        print(f"Balance: {self.balance}")
        return self 
# 4 - yield_interest(self) - 
# increases the account balance by the current balance * the interest rate 
# (as long as the balance is positive)

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_balance()


# Create 2 accounts 

bank_account1 = BankAccount(0.25,100)
bank_account2 = BankAccount(0.99,4)
#To the first account, make 3 deposits and 1 withdrawal,
# then yield interest and display the account's info all in one line of code (i.e. chaining)

#to check arguments
# bank_account1.deposit(123).display_account_balance().deposit(200).display_account_balance().deposit(255).display_account_balance().withdraw(600).display_account_balance().yield_interest().display_account_balance()
bank_account1.deposit(123).deposit(200).deposit(255).withdraw(600).yield_interest().display_account_balance()

# To the second account, make 2 deposits and 4 withdrawals, 
# then yield interest and display the account's info all in one line of code (i.e. chaining)

#to check arguments
# bank_account2.deposit(1000).display_account_balance().deposit(9025).display_account_balance().withdraw(2000).display_account_balance().withdraw(444).display_account_balance().withdraw(123).display_account_balance().withdraw(200).display_account_balance().yield_interest().display_account_balance()
bank_account2.deposit(1000).deposit(9025).withdraw(2000).withdraw(444).withdraw(123).withdraw(200).yield_interest().display_account_balance()

# Ninja Bonus

BankAccount.print_all_accounts()








