# Dota 2 Statics
Building a program that will receive a player's ID and return the last games played with statics that can help someone prepare or learn from the player. I do not own the API beign used. It belongs to [Joshua Duffy](https://github.com/joshuaduffy).

## Table of contents
- [Dependencies](https://github.com/divinoob/DotaScene#what-do-i-need-to-use-it)
- [Modifications on files](https://github.com/divinoob/DotaScene#modifications-on-files)
- [Functions explained](https://github.com/divinoob/DotaScene#functions-explained)

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
You will need to change the fileDirectory variable (line 10 on file dotaStats.py) and put your directory to the folder where the txt file that you want all the information to be saved, and change the accountDirectory as well. For exemple:

`
	fileDirectory = "C:\\Users\\Vinícius\\Documents\\UFPE\\Coding\\Python\\Dota\\txtResults\\"
`

That's the file path to the folder where my txt file is.

### Functions explained
**getMatchHistory**: Saves the match history of a certain steam account

**organizeMatches**: Receives a list of matches and the index to access the match in the array and it returns that match's ID

**getPlayerInfo**: Receives the match and access the player with the given account ID. Takes all the wanted information from it and pass it as parameter to another function called writeInFile.

**main**: Calls the other functions to save all the information on the TXT for all the matches saved

**findFile**: Looks for a file with the accountID provided as name, returns true if finds it

**getMatchDetails**: Receives a match list and the target account ID and gathers the information about that player

**login**: Receives your account ID and checks if there is a folder for it, if not, it creates, if there is, keeps going.

**printResults**: Writes the results of the query in a txt file, all at once

**greetings**: Opener function, decides what the program will do with an input from the user

**optionOne**: Gathers the information of a player last games and saves on a txt (Using the past functions)

**updateAccountOne**: Updates the account txt file to save that that person has consulted the application about someones last games
