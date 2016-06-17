# Dota 2 Statics
Building a program that will receive a player's ID and return the last games played with statics that can help someone prepare or learn from the player. I do not own the API beign used. It belongs to [Joshua Duffy](https://github.com/joshuaduffy).


## Table of contents
- [Goals](https://github.com/divinoob/DotaScene#goals)
- [JSON Usage](https://github.com/divinoob/DotaScene#json-usage)
- [Summary](https://github.com/divinoob/DotaScene#summary)

## Goals
As I am coding this little project of mine, I can see it beign used by small groups of peoples who want to keep track of themselves and their friends as well. And I see it beign used by big groups like an actual Pro team to keep track of the team and oponents in a fast, usable and simple way. We'll see how it actually works out

## JSON usage
I'm using json files to fufil the need of having stored players ID related with their name in-game. I can add and delete users from a json file as for now. Later on I'll be trying to implement a 'list' function in order to show all the players saved in that file. Might even save more information about the players in this file.

## Summary
Currently working with six different python files.

**dotastats.py** is my "runner" file, that basicly calls another file to fufil the needs of the user.

**fileOutputFunctions.py** is a file where I'm dealing with all (or almost all) functions related to file reading or file writing (not inclunding JSON)

**greetings.py** is where I can check if the user is already saved on our database, if not, I can save his information on JSON file and create his account file where I'll be saving all the information on how he is using the program (don't know why, just think it might be useful later on)

**jsonFunctions.py** is pretty much the same as fileOutputFunctions but it deals directly with my json files (now is just the players file), will do some minor changes to be adaptable to more than one json file and not ust players.json

**01.py** is where all the coding actually happens and it uses the API. It's called when the user asks to receive the game history of a certain player and saves it in a file.

**02.py** almost the same as 01.py but for the second option, where the user wants to do something with the json file, either add someone new or delete or just check if someone is there already.
