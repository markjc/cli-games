'''
------------------------------------------------------------------------------
The Convo class contains conversational elements for the computer to use when interacting with a player. They are general in nature and can be applied
to most in-game scenarios. This class will be invoked during a game, and the attribute lists will be indexed randomly during play. Generally speaking
unless one plays several iterations of these games, they should see a good mix of conversational elements to make the game more life-like. 
"Generally Speaking"
------------------------------------------------------------------------------
Mark Crabtree - 07/15/19

'''


class Convo:
    
    def __init__(self):
        self.greetings = ["Hey there!....I see You wish to play!", "You are no match for me!... Let's Play!"]
        self.taunts = ["Uh oh! ... That was a bad move!", "Oh come on! You can do better than that!"]
        self.losses = ["Oh look, I won!...I knew I would!", ]
        self.wins = ["Oh darn. Looks like I lost.", "Wow. didn't see that coming!"]
        self.congratulations = ["Well, I suppose congratulations are in order.", "You are a worthy foe! Good Job"]