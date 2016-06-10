# Dota 2 Statics
Building a program that will receive a player's ID and return the last games played with statics that can help someone prepare or learn from the player. I do not own the API beign used. It belongs to [Joshua Duffy](https://github.com/joshuaduffy).

## What do I need to use it?
- The absolute first thing you will need to use this application is to have an [Steam API key](https://steamcommunity.com/dev/apikey).
- You need to download the [dota2api](https://github.com/joshuaduffy/dota2api).
- You need to download the [Python](https://www.python.org/downloads/) language from their website.
- I'm currently working on some changes so that you won't need to download both python and API in order to run the application
- Run on your CMD while under the folder where you downloaded my application:
`
	python dotaStats.py
`

## Modifications on files
You will need to change the fileDirectory variable (line 10 on file dotaStats.py) and put your directory to the folder where the txt file that you want all the information to be saved. For exemple:
`
	fileDirectory = "C:\\Users\\Vinícius\\Documents\\UFPE\\Coding\\Python\\Dota\\txtResults\\"
`
That's the file path to the folder where my txt file is.

### Functions explained
**initialise**: Saves the match history of a certain steam account
**organizeMatches**: Receives a list of matches and the index to access the match in the array and it returns that match's ID
**getPlayerInfo**: Receives the match and access the player with the given account ID. Takes all the wanted information from it and pass it as parameter to another function called writeInFile.
**writeInFile**: Takes all the information passed and saves it on the TXT file
**main**: Calls the other functions to save all the information on the TXT for all the matches saved