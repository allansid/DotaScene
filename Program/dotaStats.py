# Owner: Vinícius Aguiar de Oliveira
# Program I'm coding to learn the dota2api and maybe use it afterwards as an opening to start on the e-sports scence, you never know.

##################IMPORTS#####################
import dota2api
import os
from datetime import datetime
##############################################

################GLOBAL VARIABLES################
fileDirectory = "C:\\Users\\Vinícius\\Documents\\UFPE\\Coding\\Python\\Dota\\txtResults\\"
accountDirectory = "C:\\Users\\Vinícius\\Documents\\UFPE\\Coding\\Python\\Dota\\Accounts\\"
responseArray = []
################################################

# First thing to code: Write down all the relevant info about one player in one match in a txt file

def findFile(name, path):
	for root, dirs, files in os.walk(path):
		if name in files:
			return True

def getMatchHistory(targetAccountID):
	while (1):
		try:
			matchList = api.get_match_history(account_id=targetAccountID)
			print("We got the match history with success")
			break
		except:
			print("Error on getting match history")
	return (matchList)

def organizeMatches(matches, index):
	match = matches[index]
	return (match['match_id'])

def getPlayerInfo(match, targetAccountID):
	players = match['players']
	x = 0
	while(1):
		player = players[x]
		if (player['account_id'] == targetAccountID):
			responseArray.append(player['account_id'])
			break
		x = x + 1

	responseArray.append(player['hero_name'])
	responseArray.append(player['kills'])
	responseArray.append(player['deaths'])
	responseArray.append(player['assists'])
	responseArray.append(player['last_hits'])
	responseArray.append(player['denies'])


	#writeInFile(str(playerID), heroName, str(killNumber), str(assistNumber), str(deathNumber), str(lastHits), str(denies))

def printResults():
	aux = 0
	for x in range(0, 100):
		with open(fileDirectory + str(responseArray[0]) + ".txt", "a") as toCreate:
			toCreate.write(str(responseArray[0]) + " as " + str(responseArray[aux+1]) + "\n")
			toCreate.write(str(responseArray[aux+2]) + "/" + str(responseArray[aux+3]) + "/" + str(responseArray[x+4]) + "\n")
			toCreate.write(str(responseArray[aux+5]) + "/" + str(responseArray[aux+6]) + "\n\n")
		aux = aux + 7

def writeInFile(playerID, heroName, killNumber, assistNumber, deathNumber, lastHits, denies):
	with open(fileDirectory + playerID + ".txt", "a") as toCreate:
		toCreate.write(playerID + " as " + heroName + "\n")
		toCreate.write(killNumber + "/" + deathNumber + "/" + assistNumber + "\n")
		toCreate.write(lastHits + "/" + denies + "\n\n")

def getMatchDetails(matchList, targetAccountID):
	matches = matchList['matches']
	index = matchList['num_results']
	for x in range(0, index): # Change it up to index
		matchAux = organizeMatches(matches, x)
		while(1):
			try:
				getPlayerInfo(api.get_match_details(matchAux), targetAccountID)
				print("We got match number " + str(x + 1) + " with success")
				break
			except:
				print("Error on getting match number " + str(x + 1))

def greetings():
	print("Type 1 to save last matches played by a certain account")
	print("Type 0 to quit")
	option = int(input())
	return option

def login():
	print("What's YOUR account ID")
	myAccountID = int(input())
	if (findFile(str(myAccountID) + ".txt", accountDirectory)):
		return myAccountID
	else:
		print("It's your first time here, let me create your folder")
		print("We will always save what you're doing in your personal folder")
		with open(accountDirectory + str(myAccountID) + ".txt", "a") as createAccount:
			createAccount.write("This file will store all the actions taken by the user " + str(myAccountID) + "\n\n\n")
		return myAccountID

def optionOne():
	print("What's the account ID?")
	targetAccountID = int(input())
	matchList = getMatchHistory(targetAccountID)
	getMatchDetails(matchList, targetAccountID)
	printResults()
	return targetAccountID

def updateAccountOne(myAccountID, targetAccountID):
	nowTime = datetime.now()
	with open(accountDirectory + str(myAccountID) + ".txt", "a") as saveConsult:
		saveConsult.write("("+str(nowTime.day) + "/" + str(nowTime.month) + "/" + str(nowTime.year) + " - " + str(nowTime.hour) + ":" + str(nowTime.minute) + ") - " + str(myAccountID) + " user has consulted " + str(targetAccountID) + " last played matches\n")

def main():
	myAccountID = login()
	option = greetings()
	if (option == 0):
		return
	elif (option == 1):
		targetAccountID = optionOne()
		updateAccountOne(myAccountID, targetAccountID)

##########################RUNNER##########################
print("What is your API Key?")
apiKey = input()
api = dota2api.Initialise(apiKey)
main()
printResults()
##########################################################
