#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 10:03:04 2019
Classic Games Terminal

This application will allow you to play classic games in the command line
As new games are added, this main program will be used to interact with
the individual classes.
@author: markjc
"""
###########################################
#   Import Packages, Modules, and Games   #
###########################################
import sys, os, time
import rps

#####################################################
#   Define Global Constants, Variables, and Lists   #
#####################################################






###########################################
#                Main Menu                #
###########################################
def runGame(userInput):
    ### Take user input and Map it to a runnable game - then engage that class
    if userInput == 1:
        #Run Game 1: Rock Paper Scissors
        newGame = rps.Game()
        newGame.intro()
        newGame.gameLoop()
        mainMenu()
    elif userInput == 2:
        sys.exit()
    else:
        mainMenu()


###########################################
#                Main Menu                #
###########################################
def mainMenu():
    userInput = 0
    while True:
        os.system('clear')
        print('#################################################')
        print('#                                               #')
        print('#   Welcome to the Classic Games Command Line   #')
        print('#               by: Mark Crabtree               #')
        print('#                                               #')
        print('#       Please choose a game by entering        #')
        print('#                a number below.                #')
        print('#                                               #')
        print('#################################################')
        print()
        print('            1. Rock, Paper, Scissors    ')
        print('            2. Exit      ')
       
        
        
        ### Input Validation ###
        while True:
            try:
                
                userInput = int(input('->'))
            except ValueError:
                print("Please enter a valid selection: ")
                time.sleep(0.8)
                continue
            else:
                break
        
        #### Launch the appropriate game based on user selection
        runGame(userInput)


###########################################
#                Main Loop                #
###########################################
while True:
    os.system('clear')
    mainMenu()
    
sys.exit()

