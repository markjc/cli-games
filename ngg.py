'''
ATTENTION:
    
This File is a Work in Progress to implement the NUmber Guessing Game.
It was derived from the template of another class and still contains elements of that code
This notice will be removed upon completion of the task. 
'''

#import built in modules
import random, os, sys
from time import sleep
#import local modules
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
        self.startRun = True
        self.WINS = 0
        self.LOSSES = 0
        

###########################################
#         ----------------------          #
#           Game Introduction             #
#         ----------------------          #
###########################################    
    def intro(self):
        ### Clear the terminal and display the Game Title and Intro ###
        printer = printerObj.TPrinter()
        os.system('clear')
        print('*************************************************')
        print("*                  Let's Play:                  *")
        print('*************************************************')
        
        ### If this is the First play, Implement Title Animation ###
        if self.firstPlay == True:
            printer.tprint('              '+self.gameTitle+'             \n',0.02)
        else:
            print("              "+self.gameTitle+"              ")
        printer.tprint("          Wins: " + str(self.WINS) + " - Losses: " + str(self.LOSSES) + " - Ties: " + str(self.TIES),0.01)
        print()

###########################################
#         ----------------------          #
#           Choose Difficulty             #
#         ----------------------          #
###########################################    
    def difficulty(self):
        pass

###########################################
#         ----------------------          #
#             Main Game Loop              #
#         ----------------------          #
########################################### 
       
    def gameLoop(self):
        ###define options for input and computer selection, create conversational response object, and alter firstPlay boolean
        options = ["rock","paper","scissors"]
        speak = convo.Convo()
        self.firstPlay = False
        while True:
            #Play the Game.
            playAgain = ''
            #### If it's the first play, greet the user, else continue the game.
            if self.firstPlay == True:
                print(speak.greetings[random.randint(0, len(speak.greetings)-1)])
            sleep(1)
            
            #__________________________________________________________
            
            
            
            
            #__________________________________________________________
            
            #Determine if a win condition has been reached
            result = self.checkWin(selection, choice)
            
            #Communicate the win condition to the user, and increment the appropriate counter for score generation
            if result == 'win':
                print(speak.wins[random.randint(0, len(speak.wins)-1)])
                self.WINS +=1
            elif result == 'loss':
                print(speak.losses[random.randint(0, len(speak.losses)-1)])
                self.LOSSES +=1
            
            
            #Determine if the user wants to play again, or navigate back to the main menu
            print()
            playAgain = input('Would you like to play again? -- y for yes, or n for no -->')
            if playAgain == 'y':
                os.system('clear')
                self.intro()
                continue
            else:
                break

             