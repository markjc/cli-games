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
        self.greetings = ["Hey there!....I see You wish to play!", "You are no match for me!... Let's Play!", 
                          "Okay, Let's go!", "Let's Do This!", "Shall we begin?", "Okay, Here we go.", "Let's Start.",
                          "I'm ready... Are you?", "I'm so excited to play!"]
        self.taunts = ["Uh oh! ... That was a bad move!", "Oh come on! You can do better than that!", 
                       "Is that all you got?", "Are you even trying?", "I'm not even breaking a sweat!"]
        self.losses = ["Oh look, I won!...I knew I would!", "I win, I win, I win! Yay!", "So sorry for your loss..",
                       "Better luck next time!", "Come back when you want to try again!"]
        self.wins = ["Oh darn. Looks like I lost.", "Wow. didn't see that coming!", "Oh crap, you won!", 
                     "How did you win!!!!??", "I can't believe I lost!", "Wow, that did not go as expected."]
        self.congratulations = ["Well, I suppose congratulations are in order.", "You are a worthy foe! Good Job", "That was truly amazing!",
                                "You did really well there, congrats!", "I beter look out next time we play, you're good!"]