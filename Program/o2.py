# Owner: Vinícius Aguiar de Oliveira
# Program I'm coding to learn the dota2api and maybe use it afterwards as an opening to start on the e-sports scence, you never know.

##################IMPORTS#####################
import json
import jsonFunctions
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
        if (option == 0):
            break
        elif (option == 1):
            print ("What's the name of the person you want to check?")
            name = input()
            jsonFunctions.listPlayer(name)
        elif (option == 2):
            print ("What is the name of the person you want to add?")
            name = input()
            print ("What is his/her ID?")
            ID = int(input())
            jsonFunctions.addNewPlayer(name, ID)
        elif (option == 3):
            print ("What is the name of the person you want out of the list?")
            name = input()
            jsonFunctions.deletePlayer(name)
