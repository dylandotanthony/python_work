class User:
    def __init__ (self, first_name, last_name, email, age):
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
# display_info(self) 
# Have this method print all of the users' details on separate lines.
    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member:{self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")
        return self
# enroll(self) -
# Have this method change the user's member status to True and set 
# their gold card points to 200.
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self
# spend_points(self, amount) -
# have this method decrease the user's points by the amount specified.
    def spend_points(self,amount):
        self.gold_card_points = self.gold_card_points - amount
        return self

user_dylan = User("Dylan","Stalcar","dylan@mail.com",29)
user1 = User("Zankou","anthony","zankou@mail.com",4)
user_alexis = User("Alexis", "Stalcar", "alexis@mail.com", 26)

#tests
user_alexis.display_info().enroll().spend_points(150).display_info()
# user_alexis.enroll()
# user_alexis.display_info()
# user_alexis.spend_points(150)
# user_alexis.display_info()
