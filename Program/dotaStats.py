# Owner: Vinícius Aguiar de Oliveira
# Program I'm coding to learn the dota2api and maybe use it afterwards as an opening to start on the e-sports scence, you never know.

##################IMPORTS#####################
import dota2api
import os
##############################################

################GLOBAL VARIABLES################
fileDirectory = "C:\\Users\\Vinícius\\Documents\\UFPE\\Coding\\Python\\Dota\\txtResults\\"
accountDirectory = "C:\\Users\\Vinícius\\Documents\\UFPE\\Coding\\Python\\Dota\\Accounts\\"
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
	player = players[2]
	playerID = player['account_id']
	players = match['players']

	x = 0
	while(1):
		player = players[x]
		playerID = player['account_id']
		if (playerID == targetAccountID):
			break
		x = x + 1

	heroName = player['hero_name']

	killNumber = player['kills']
	assistNumber = player['assists']
	deathNumber = player['deaths']

	lastHits = player['last_hits']
	denies = player['denies']
	writeInFile(str(playerID), heroName, str(killNumber), str(assistNumber), str(deathNumber), str(lastHits), str(denies))

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

def main():
	myAccountID = login()
	option = greetings()
	if (option == 0):
		return
	elif (option == 1):
		optionOne()

##########################RUNNER##########################
print("What is your API Key?")
apiKey = input()
api = dota2api.Initialise(apiKey)
main()
##########################################################
