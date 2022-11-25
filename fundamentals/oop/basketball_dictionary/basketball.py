players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33, "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32, "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "", 
        "age":16, 
        "position": "P", 
        "team": "en"
    }
]

# Update the constructor to accept a dictionary with
# a single player's information instead of individual arguments for the attributes.
# Set up a new file and add the Player class with the given constructor

class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team









# Challenge 1: Update the constructor to accept a dictionary (player) as an argument
# and set the attributes using the dictionary

# Complete challenge 2: Create 3 instances of the Player class using the given dictionaries

# Complete challenge 3: Populate a new list with Player instances from the list of players.

# Ninja Bonus: Add an @class method called get_team(cls, team_list) that,
# given a list of dictionaries populates and returns a new list of Player objects.