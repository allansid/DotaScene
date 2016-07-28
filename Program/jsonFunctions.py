# coding: utf-8
# Owner: Vinícius Aguiar de Oliveira
# Program I'm coding to learn the dota2api and maybe use it afterwards as an opening to start on the e-sports scence, you never know.

##################IMPORTS#####################
import json
import fileOutputFunctions
##############################################

################GLOBAL VARIABLES################
jsonDirectory = '../dictID/players.json'
################################################

def addNewPlayer(name, ID):
    jsonToFile = {'Name': name, 'ID': ID}
    data = fileOutputFunctions.jsonLoadFile(jsonDirectory)
    data['players'].append(jsonToFile)
    fileOutputFunctions.jsonWriteFile(jsonDirectory, data)
    print("The player " + name + " with ID " + str(ID) + " has been saved to our database")

def deletePlayer(name):
    data = fileOutputFunctions.jsonLoadFile(jsonDirectory)
    for x in range (0, len(data['players'])):
        if (data['players'][x]['Name'] == name):
            del data['players'][x]
            print("Player " + name + " has been deleted")
            break
        elif (len(data['players']) - x == 1):
            print("This player is not in our database, you are good to go")
    fileOutputFunctions.jsonWriteFile(jsonDirectory, data)

def listPlayer(name):
    data = fileOutputFunctions.jsonLoadFile(jsonDirectory)
    for x in range (0, len(data['players'])):
        if (data['players'][x]['Name'] == name):
            print (name + "'s ID is " + str(data['players'][x]['ID']))
            break
        elif (len(data['players']) - x == 1):
            print("This player is not in our database")

def existsPlayer(ID):
    data = fileOutputFunctions.jsonLoadFile(jsonDirectory)
    for x in range(0, len(data['players'])):
        if (data['players'][x]['ID'] == ID):
            return True
        elif (len(data['players']) - x == 1):
            return False

def getName(ID):
    data = fileOutputFunctions.jsonLoadFile(jsonDirectory)
    for x in range(0, len(data['players'])):
        if (data['players'][x]['ID'] == ID):
            return data['players'][x]['Name']
        elif (len(data['players']) - x == 1):
            return None
