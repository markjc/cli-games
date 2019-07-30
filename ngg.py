"""
Initial Release of Number Guessing Game complete 7/29
Additional Features to add in future versions:

Least number of guesses leaderboard.
Add Limited guesses mode. 
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#         ----------------------          #
#       Import Packages, and Modules      #
#         ----------------------          #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
import random, os, sys
from time import sleep

import convo
import TPrinter as printerObj


class Game:
    
    
###########################################
#         ----------------------          #
#          Class Initialization           #
#         ----------------------          #
###########################################
    def __init__(self):
        #Define class variables and constants
        self.gameTitle = 'NUMBER GUESSING GAME'
        self.firstPlay = True
        self.initialRun = True
        self.difficulty = {"1": 10, "2": 50, "3": 100, "4": 500, "5": 1000, "6": 1000000}
        

###########################################
#         ----------------------          #
#           Game Introduction             #
#         ----------------------          #
###########################################    
    def intro(self):
        ### Clear the terminal and display the Game Title and Intro ###
        printer = printerObj.TPrinter()
        os.system('cls' if os.name == 'nt' else 'clear')
        print('*************************************************')
        print("*                  Let's Play:                  *")
        print('*************************************************')
        
        ### If this is the First play, Implement Title Animation ###
        if self.firstPlay:
            printer.tprint('              '+self.gameTitle+'             \n',0.02)
        else:
            print("              "+self.gameTitle+"              ")
        print()

###########################################
#         ----------------------          #
#           Choose Difficulty             #
#         ----------------------          #
###########################################    
    def set_difficulty(self):
        self.initialRun = False
        print()
        print("Please Choose a Number Difficulty: ")
        print("1. Super Easy [1-10]")
        print("2. Easy [1-50]")
        print("3. Normal [1-100]")
        print("4. Hard [1-500]")
        print("5. Very Hard [1-1000]")
        print("6. Super Epic Crazy Hard [1-1,000,000]")
        userInput = input("--> ")
        while int(userInput) not in range(1, 7):
            print("Please enter a valid choice: 1-6")
            userInput = input("--> ")
        return self.difficulty[userInput]
        

###########################################
#         ----------------------          #
#-----||      Main Game Loop       ||-----#
#         ----------------------          #
########################################### 
       
    def gameLoop(self):

        ### create conversational response object, and alter firstPlay boolean
        
        speak = convo.Convo()
        self.firstPlay = False

        while True:
            # If it is the initial play of the game, allow the user to select the Difficulty
            if self.initialRun:
                limit = self.set_difficulty()
            #Play the Game.
            playAgain = ''
            #### If it's the first play, greet the user, else continue the game.
            if self.firstPlay:
                print(speak.greetings[random.randint(0, len(speak.greetings)-1)])
            sleep(1)
            
            #__________________________________________________________
            
            userGuess = 0
            targetNum = random.randint(1, limit)

            while userGuess != targetNum:
                print("Please guess a number between 1 and " + str(limit))
                userGuess = int(input("--> "))

                if userGuess < targetNum:
                    print("Nope, The number is Higher.")
                elif userGuess > targetNum:
                    print("Nope, The number is Lower.")
                else:
                    print("Congratulations! You Guessed it!")
                    self.initialRun = True
                    break

            #__________________________________________________________

            
            
            #Determine if the user wants to play again, or navigate back to the main menu
            print()
            playAgain = input('Would you like to play again? -- y for yes, or n for no -->')
            if playAgain == 'y':
                os.system('cls' if os.name == 'nt' else 'clear')
                self.intro()
                continue
            else:
                break

             