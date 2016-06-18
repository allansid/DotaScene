# Owner: Vinícius Aguiar de Oliveira
# Program I'm coding to learn the dota2api and maybe use it afterwards as an opening to start on the e-sports scence, you never know.

##################IMPORTS#####################
from datetime import datetime
import jsonFunctions
import fileOutputFunctions
##############################################

################GLOBAL VARIABLES################
responseArray = []
################################################

def optionOne(api, myAccountID, fileDirectory):
	print("What's the account ID?")
	targetAccountID = int(input())
	matchList = getMatchHistory(targetAccountID, api)
	getMatchDetails(matchList, targetAccountID, api)
	name = printResults(myAccountID, fileDirectory)

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
			responseArray.append(player['account_id'])
			break
		x = x + 1

	responseArray.append(player['hero_name'])
	responseArray.append(player['kills'])
	responseArray.append(player['deaths'])
	responseArray.append(player['assists'])
	responseArray.append(player['last_hits'])
	responseArray.append(player['denies'])

def printResults(myAccountID, fileDirectory):
	name = jsonFunctions.getName(myAccountID)
	if (name == None):
		return
	aux = 0
	writer = 'w'
	for x in range(0, 100):
		content = (name + " as " + str(responseArray[aux+1]) + "\n" + str(responseArray[aux+2]) + "/" + str(responseArray[aux+3]) + "/" +
		str(responseArray[x+4]) + "\n" + str(responseArray[aux+5]) + "/" + str(responseArray[aux+6]) + "\n\n")
		if (x != 0):
			writer = 'a'
		fileOutputFunctions.optionOneWrite(name, content, fileDirectory, writer)
		aux = aux + 7
	return name
