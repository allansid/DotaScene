# Owner: Vinícius Aguiar de Oliveira
# Program I'm coding to learn the dota2api and maybe use it afterwards as an opening to start on the e-sports scence, you never know.

##################IMPORTS#####################
import dota2api
##############################################

#################GLOBAL VARIABLES#################
apiKey = "C97C5017DD6A5424C3271ABAA2B0E0AC"
matchID = 2391959487
accountID = 215907469
fileDirectory = "C:\\Users\\Vinícius\\Documents\\UFPE\\Coding\\Python\\Dota\\txtResults\\"
##################################################

# First thing to code: Write down all the relevant info about one player in one match in a txt file

api = dota2api.Initialise(apiKey)

def initialise(id):
	matchList = api.get_match_history(account_id=accountID)
	return (matchList)

def organizeMatches(matches, index):
	match = matches[index]
	return (match['match_id'])

def getPlayerInfo(match):
	players = match['players']
	player = players[2]
	playerID = player['account_id']
	players = match['players']

	x = 0
	while(1):
		player = players[x]
		playerID = player['account_id']
		if (playerID == 215907469):
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

def main():
	matchList = initialise(matchID)
	matches = matchList['matches']
	index = matchList['num_results']
	for x in range(0, index):
		matchAux = organizeMatches(matches, x)
		getPlayerInfo(api.get_match_details(matchAux))

main()


