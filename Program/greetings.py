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


def login():
	print("\nWhat's YOUR account ID?")
	myAccountID = int(input())
	exists = jsonFunctions.existsPlayer(myAccountID)
	if (exists):
		return myAccountID
	else:
		print("\nIt's your first time here, let me create your folder")
		print("What is your name in game?\n")
		name = input()
		jsonFunctions.addNewPlayer(name, myAccountID)
		now = datetime.now()
		adminContent = "(" + str(now.day) + "/" + str(now.month) + "/" + str(now.year) + " - " + str(now.hour) + ":" + str(now.minute) + ") - " + "New account with name " + name + " and ID " + str(myAccountID) + " has been created\n"
		fileOutputFunctions.updateAdminFile(adminContent)
		return myAccountID

def greetings():
	print("\nType 1 to save last matches played by a certain account")
	print("Type 2 to access the ID's saved")
	print("Type 0 to quit\n")
	option = int(input())
	return option
