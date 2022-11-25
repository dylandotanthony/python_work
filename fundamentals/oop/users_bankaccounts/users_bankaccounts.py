class BankAccount:
    # variable
    accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        # need to append to link instances to variable 
        BankAccount.accounts.append(self)

# increases the account balance by the given amount
    def deposit(self, amount):
        self.balance += amount
        return self
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
# print to the console: eg. "Balance: $100"
    def display_account_balance(self):
        return f"{self.balance}"
        
# increases the account balance by the current balance * the interest rate if positive
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self
# use a classmethod to print all instances of a Bank Account's info
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_balance()

# Update the User class __init__ method
# Add a make_deposit method to the User class that calls on it's bank account's instance methods.
# Add a make_withdrawal method to the User class that calls on it's bank account's instance methods.

# SENSEI BONUS: Allow a user to have multiple accounts; 
# update methods so the user has to specify which account they are withdrawing or depositing to
class User:
    def __init__(self, name):
        self.name = name
        self.account = {
            "checking" : BankAccount(0.02, 1100),
            "savings" : BankAccount(.55, 1200)
        }

    def display_user_balance(self):
        print(f"User: {self.name}, Checking  Balance: ${self.account['checking'].display_account_balance()}")
        print(f"User: {self.name}, Savings Balance: ${self.account['savings'].display_account_balance()}")
    
    def trasfer_money(self, amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self

# SENPAI BONUS: Add a transfer_money(self, amount, other_user) 
# method to the user class that takes an amount and a different User instance, 
# and transfers money from the user's account into another user's account.
    def transfer_the_money(self, amount, other_user):
        self.account['checking'].balance = self.account['checking'].balance - amount
        other_user.balance = other_user.balance + amount 
        return self

# Add a display_user_balance method to the User class that displays user's account balance

dylan = User("Dylan")
crystal = User("Crystal")

# dylan.account['checking'].deposit(400)

crystal.transfer_the_money(200,dylan.account['checking'])
crystal.display_user_balance()
dylan.display_user_balance()






