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
        self.gameTitle = 'ROCK, PAPER, SCISSORS!'
        self.firstPlay = True
        self.WINS = 0
        self.LOSSES = 0
        self.TIES = 0

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
#          Check Win Condition            #
#         ----------------------          #
###########################################   

        
    def checkWin(self, selection, choice):
        #determine if Win,Loss,or Tie conditions are met
        ### USER CHOOSES ROCK ###
        if choice == 'rock':
            if selection == 'rock':
                return 'tie'
            elif selection == 'paper':
                return 'loss'
            else:
                return 'win'
            
        ### USER CHOOSES PAPER ###    
        elif choice == 'paper':
            if selection == 'paper':
                return 'tie'
            elif selection == 'scissors':
                return 'loss'
            else:
                return 'win'
        
        ### USER CHOOSES SCISSORS ###
        else:
            if selection == 'scissors':
                return 'tie'
            elif selection == 'rock':
                return 'loss'
            else:
                return 'win'

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
            
            ##obtain user's choice
            print("Go Ahead, choose: rock - paper - scissors\n")
            choice = input()
            
            
            #Validate Input
            while choice not in options:
                print("Please enter a valid selection: ")
                sleep(0.8)
                choice = input()
            
            #Make computer selection
            selection = options[random.randint(0, 2)]
            
            #Display Choices from User and Computer
            print("You chose: " + choice)
            sleep(.8)
            print("I chose: " + selection)
            sleep(.96)
            
            #Determine if a win condition has been reached
            result = self.checkWin(selection, choice)
            
            #Communicate the win condition to the user, and increment the appropriate counter for score generation
            if result == 'win':
                print(speak.wins[random.randint(0, len(speak.wins)-1)])
                self.WINS +=1
            elif result == 'loss':
                print(speak.losses[random.randint(0, len(speak.losses)-1)])
                self.LOSSES +=1
            else:
                print("It's a Tie!")
                self.TIES +=1
            
            #Determine if the user wants to play again, or navigate back to the main menu
            print()
            playAgain = input('Would you like to play again? -- y for yes, or n for no -->')
            if playAgain == 'y':
                os.system('clear')
                self.intro()
                continue
            else:
                break

             