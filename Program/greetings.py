# Owner: Vinícius Aguiar de Oliveira
# Program I'm coding to learn the dota2api and maybe use it afterwards as an opening to start on the e-sports scence, you never know.

##################IMPORTS#####################
import os
import jsonFunctions
import fileOutputFunctions
from datetime import datetime
##############################################

################GLOBAL VARIABLES################

################################################


def login(accountDirectory):
	print("\nWhat's YOUR account ID?")
	myAccountID = int(input())
	exists = jsonFunctions.existsPlayer(myAccountID)
	if (exists):
		return myAccountID
	else:
		print("\nIt's your first time here, let me create your folder")
		print("What is your name in game?\n")
		name = input()
		print("\nWe will always save what you're doing in your personal folder")
		content = "This file will store all the actions taken by the user " + name + "\n\n\n"
		fileOutputFunctions.createAccountFile(myAccountID, name, content, accountDirectory)
		return myAccountID

def greetings():
	print("\nType 1 to save last matches played by a certain account")
	print("Type 2 to access the ID's saved")
	print("Type 0 to quit\n")
	option = int(input())
	return option
