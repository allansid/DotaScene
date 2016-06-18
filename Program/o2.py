# Owner: Vinícius Aguiar de Oliveira
# Program I'm coding to learn the dota2api and maybe use it afterwards as an opening to start on the e-sports scence, you never know.

##################IMPORTS#####################
import json
import jsonFunctions
import sys
from datetime import datetime
##############################################

################GLOBAL VARIABLES################

################################################

def optionTwo(myAccountID):
    while (1):
        print ("\nType 1 to search an ID")
        print ("Type 2 to add a ID to the list")
        print ("Type 3 to remove a saved AD")
        print ("Type 0 to go back\n")
        option = int(input())
        choice = "no"
        if (option == 0):
            break
        elif (option == 1):
            print ("What's the name of the person you want to check?")
            nameCheck = input()
            jsonFunctions.listPlayer(nameCheck)
        elif (option == 2):
            print ("What is the name of the person you want to add?")
            nameAdd = input()
            print ("What is his/her ID?")
            ID = int(input())
            jsonFunctions.addNewPlayer(nameAdd, ID)
        elif (option == 3):
            name = jsonFunctions.getName(myAccountID)
            print ("What is the name of the person you want out of the list?")
            nameDelete = input()
            if (nameDelete == name):
                print("If you delete yourself from the players file, you will be forced to leave the program, wish to continue?")
                choice = input()
            jsonFunctions.deletePlayer(nameDelete)
            if (choice.lower() == "yes"):
                sys.exit("You deleted yourself from the list. You can get back in at anytime!")
