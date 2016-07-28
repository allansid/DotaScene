# coding: utf-8
# Owner: Vinícius Aguiar de Oliveira
# Program I'm coding to learn the dota2api and maybe use it afterwards as an opening to start on the e-sports scence, you never know.

##################IMPORTS#####################
import jsonFunctions
import fileOutputFunctions
from datetime import datetime
##############################################

################GLOBAL VARIABLES################
responseArray = []
################################################

def optionOne(api, myAccountID, fileDirectory):
	#global resposnseArray
	del responseArray[:]
	print("What's the account ID?")
	targetAccountID = int(raw_input())
	matchList = getMatchHistory(targetAccountID, api)
	getMatchDetails(matchList, targetAccountID, api)
	name = printResults(myAccountID, fileDirectory, targetAccountID)

def getMatchHistory(targetAccountID, api):
	while (1):
		try:
			matchList = api.get_match_history(account_id=targetAccountID)
			print("\nWe got the match history with success")
			break
		except:
			print("Error on getting match history")
	return (matchList)

def getMatchDetails(matchList, targetAccountID, api):
	matches = matchList['matches']
	index = matchList['num_results']
	for x in range(0, index):
		matchAux = organizeMatches(matches, x)
		while(1):
			try:
				getPlayerInfo(api.get_match_details(matchAux), targetAccountID)
				print("We got match number " + str(x + 1) + " with success")
				break
			except:
				print("Error on getting match number " + str(x + 1))

def organizeMatches(matches, index):
	match = matches[index]
	return (match['match_id'])

def getPlayerInfo(match, targetAccountID):
	players = match['players']
	x = 0
	while(1):
		player = players[x]
		if (player['account_id'] == targetAccountID):
			responseArray.append(player['hero_name'])
			responseArray.append(player['kills'])
			responseArray.append(player['deaths'])
			responseArray.append(player['assists'])
			responseArray.append(player['last_hits'])
			responseArray.append(player['denies'])
			break
		x = x + 1

def printResults(myAccountID, fileDirectory, targetAccountID):
	print (myAccountID, targetAccountID)
	name = jsonFunctions.getName(myAccountID)
	if (name == None):
		print ("You have to have the player saved in our list first. Try again")
		return
	aux = 0
	writer = 'w'
	for x in range(0, 100):
		content = str(targetAccountID) + " as " + str(responseArray[aux]) + "\n" + str(responseArray[aux+1]) + "/" + str(responseArray[aux+2]) + "/" + str(responseArray[aux+3]) + "\n" + str(responseArray[aux+4]) + "/" + str(responseArray[aux+5]) + "\n\n"
		if (x != 0):
			writer = 'a'
		fileOutputFunctions.optionOneWrite(targetAccountID, content, fileDirectory, writer)
		aux = aux + 6

	now = datetime.now()
	adminContent = "(" + str(now.day) + "/" + str(now.month) + "/" + str(now.year) + " - " + str(now.hour) + ":" + str(now.minute) + ") - " + name + ", player of the ID " + str(myAccountID) + " has consulted " + str(targetAccountID) + " last played matches\n"
	fileOutputFunctions.updateAdminFile(adminContent)

	return name
