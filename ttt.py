#import built in modules
import random, os
from time import sleep
#import local modules
import convo
import TPrinter as printerObj


class Game:
    
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#         ----------------------          #
#          Class Initialization           #
#         ----------------------          #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def __init__(self):
        #Define class variables and constants
        self.gameTitle = 'TIC - TAC - TOE!'
        self.firstRun = True
        self.WINS = 0
        self.LOSSES = 0
        self.TIES = 0
        self.gameboard = [['*','*','*'],
                          ['*','*','*'],
                          ['*','*','*']]
        self.avail_moves = [True,True,True,True,True,True,True,True,True]
        self.playerMarker = 'X'
        self.cpuMarker = 'O'
        self.firstPlay = True
        self.currentPlayer = 'user'
        self.difficulty = 1 #TODO: Adjust later to switch to different levels of difficulty. 
        self.remainingMoves = 9

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#         ----------------------          #
#           Game Introduction             #
#         ----------------------          #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#    
    def intro(self):
        ### Clear the terminal and display the Game Title and Intro ###
        printer = printerObj.TPrinter()
        os.system('cls' if os.name == 'nt' else 'clear')
        print('*************************************************')
        print("*                  Let's Play:                  *")
        print('*************************************************')
        
        ### If this is the First play, Implement Title Animation ###
        if self.firstRun == True:
            printer.tprint('                 '+self.gameTitle+'             \n',0.02)
            printer.tprint("          Wins: " + str(self.WINS) + " - Losses: " + str(self.LOSSES) + " - Ties: " + str(self.TIES),0.01)
        else:
            print("                 "+self.gameTitle+"              ")
            print("          Wins: " + str(self.WINS) + " - Losses: " + str(self.LOSSES) + " - Ties: " + str(self.TIES))
        
        print()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#         ----------------------          #
#          Check Win Condition            #
#         ----------------------          #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#   

        
    def checkWin(self, gamePiece):
        #Determine if Win,Loss,or Tie conditions are met
        
        #Check by Center Location (5)
        if self.gameboard[1][1] == gamePiece:
            if self.gameboard[0][0] == gamePiece and self.gameboard[2][2] == gamePiece:
                return True
            elif self.gameboard[0][1] == gamePiece and self.gameboard[2][1] == gamePiece:
                return True
            elif self.gameboard[0][2] == gamePiece and self.gameboard[2][0] == gamePiece:
                return True
            elif self.gameboard[1][0] == gamePiece and self.gameboard[1][2] == gamePiece:
                return True
        
        
        #Check by Edge Locations (s)
        if self.gameboard[0][1] == gamePiece:
            if self.gameboard[0][0] == gamePiece and self.gameboard[0][2] == gamePiece:
                return True
        elif self.gameboard[1][0] == gamePiece:
            if self.gameboard[0][0] == gamePiece and self.gameboard[2][0] == gamePiece:
                return True
        elif self.gameboard[1][2] == gamePiece:
            if self.gameboard[0][2] == gamePiece and self.gameboard[2][2] == gamePiece:
                return True
        elif self.gameboard[2][1] == gamePiece:
            if self.gameboard[2][0] == gamePiece and self.gameboard[2][2] == gamePiece:
                return True
        elif self.remainingMoves == 0:
            return 'Tie'
        else:
            return False   
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#         ----------------------          #
#            Get Player Move              #
#         ----------------------          #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#   

        
    def playerMove(self):
                
        ### Get move from User, Check if its valid, and Place Marker ###
        move = int(input())
        valid = self.validMove(move)
        while not valid:
            print("That is not a valid move, please choose an open space.")
            move = int(input())
            valid = self.validMove(move)
        self.placeMarker(move, self.playerMarker)
        self.remainingMoves -= 1
        
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#         ----------------------          #
#              Get AI Move                #
#         ----------------------          #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#   

        
    def cpuMove(self):
        #Get the CPU Move and Apply it to the current
        #state of the board
        if self.difficulty == 1:
            
            move = random.randint(1, 9)
            isValid = self.validMove(move)
            while isValid == False:
                move = random.randint(1, 9)
                isValid = self.validMove(move)
            self.placeMarker(move, self.cpuMarker)
        self.remainingMoves -= 1
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#         ----------------------          #
#            Marker Selection             #
#         ----------------------          #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#   

        
    def firstPlayFunc(self):
        ### Player Chooses Marker ###
        print()
        choice = input("Please choose X or O --> ")
        while choice != 'X' and choice != 'O':
            choice = input("Please choose X or O --> ")
        self.playerMarker = choice
        if self.playerMarker == 'X':
            self.cpuMarker = 'O'
            self.currentPlayer = 'user'
        else:
            self.cpuMarker = 'X'
            self.currentPlayer = 'cpu'
        self.firstPlay = False
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#         ----------------------          #
#           Display Game Board            #
#         ----------------------          #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#   

        
    def displayBoard(self):
        
        print()
        for i in range(0,3):
            print('|', end="", flush=True)
            for j in range(0,3):
                if j == 2:
                    print(self.gameboard[i][j] + ' | ' + '\n', end="", flush=True)
                else:
                    print(self.gameboard[i][j]+ ' | ' , end="", flush=True)
            if i < 2:
                print("------------")
        print()            
        return None

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#         ----------------------          #
#              Clear Board                #
#         ----------------------          #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 

    def clearBoard(self):
        for i in range(0,3):
            for j in range(0,3):
                self.gameboard[i][j] = '*'
        for item in range(0, 9):
            self.avail_moves[item] = True
        self.remainingMoves = 9


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#         ----------------------          #
#           Place Game Pieces             #
#         ----------------------          #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 
    
    def placeMarker(self, move, marker):
        if move < 4:
            self.gameboard[0][move-1] = marker
        elif move < 7:
            self.gameboard[1][move-4] = marker
        else:
            self.gameboard[2][move-7] = marker
        self.avail_moves[move - 1] = False
            
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#         ----------------------          #
#         Validate Selected Move          #
#         ----------------------          #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 

    def validMove(self, move):
        if self.avail_moves[move - 1]:
            return True
        else:
            return False

###########################################
#         ----------------------          #
#-----||      Main Game Loop       ||-----#
#         ----------------------          #
########################################### 
       
    def gameLoop(self):
        ###define options for input and computer selection, create conversational response object, and alter firstRun boolean
        speak = convo.Convo()
        self.firstRun = False
        
        if self.firstPlay:
            self.firstPlayFunc()
        playAgain = ''
        #### If it's the first play, greet the user, else continue the game.
        if self.firstRun == True:
            print(speak.greetings[random.randint(0, len(speak.greetings)-1)])
        sleep(1)
                    
            
        while True:
            
            ### Clear the terminal, Display Header, Display the current Board ###
            os.system('clear')
            self.intro()
            
            self.displayBoard()
            
            winState = self.checkWin(self.playerMarker)
            if winState == True:
                self.firstPlay = True
                print(speak.wins[random.randint(0, len(speak.wins)-1)])
                self.WINS +=1
                break
            elif winState == 'Tie':
                print("It's a Tie!")
                self.TIES +=1
                break
                
            winState = self.checkWin(self.cpuMarker)
            if winState == True:
                self.firstPlay = True
                print(speak.losses[random.randint(0, len(speak.losses)-1)])
                self.LOSSES +=1
                break
            elif winState == 'Tie':
                print("It's a Tie!")
                self.TIES +=1
                break
                   
            
            if self.currentPlayer == 'user':
                self.playerMove()
                self.currentPlayer = 'cpu'
            else:
                self.cpuMove()
                self.currentPlayer = 'user'
               
        
        
        
        
        
        #Determine if the user wants to play again, or navigate back to the main menu
        print()
        playAgain = input('Would you like to play again? -- y for yes, or n for no -->')
        while playAgain != 'y' and playAgain != 'n':
            playAgain = input('Would you like to play again? -- y for yes, or n for no -->')
        if playAgain == 'y':
            os.system('clear')
            self.clearBoard()
            self.gameLoop()
            
            
        

        