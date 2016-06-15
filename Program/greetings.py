# Owner: Vinícius Aguiar de Oliveira
# Program I'm coding to learn the dota2api and maybe use it afterwards as an opening to start on the e-sports scence, you never know.

##################IMPORTS#####################
import os
from datetime import datetime
##############################################

################GLOBAL VARIABLES################
fileDirectory = "C:\\Users\\Vinícius\\Documents\\UFPE\\Coding\\Python\\Dota\\txtResults\\"
accountDirectory = "C:\\Users\\Vinícius\\Documents\\UFPE\\Coding\\Python\\Dota\\Accounts\\"
################################################


def login():
	print("What's YOUR account ID")
	myAccountID = int(input())
	if (findFile(str(myAccountID) + ".txt", accountDirectory)):
		return myAccountID
	else:
		print("It's your first time here, let me create your folder")
		print("We will always save what you're doing in your personal folder\n")
		with open(accountDirectory + str(myAccountID) + ".txt", "a") as createAccount:
			createAccount.write("This file will store all the actions taken by the user " + str(myAccountID) + "\n\n\n")
		return myAccountID

def findFile(name, path):
	for root, dirs, files in os.walk(path):
		if name in files:
			return True

def greetings():
	print("Type 1 to save last matches played by a certain account")
	print("Type 2 to access the ID's saved")
	print("Type 0 to quit\n")
	option = int(input())
	return option
