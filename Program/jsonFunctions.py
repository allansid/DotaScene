# Owner: Vinícius Aguiar de Oliveira
# Program I'm coding to learn the dota2api and maybe use it afterwards as an opening to start on the e-sports scence, you never know.

##################IMPORTS#####################
import json
##############################################

################GLOBAL VARIABLES################
jsonDirectory = "C:\\Users\\Vinícius\\Documents\\UFPE\\Coding\\Python\\Dota\\dictID\\players.json"
################################################

def addNewPlayer(name, ID):
    jsonToFile = {'Name': name, 'ID': ID}
    with open(jsonDirectory) as loadFile:
        data = json.load(loadFile)
    data['players'].append(jsonToFile)
    with open(jsonDirectory, 'w') as writeFile:
        json.dump(data, writeFile, indent = 4, sort_keys = True)
    print("The player " + name + " with ID " + str(ID) + " has been saved to our database")

def deletePlayer(name):
    with open(jsonDirectory) as loadFile:
        data = json.load(loadFile)
    for x in range (0, len(data['players'])):
        if (data['players'][x]['Name'] == name):
            del data['players'][x]
            print("Player " + name + " has been deleted")
            break
        elif (len(data['players']) - x == 1):
            print("This player is not in our database, you are good to go")
    with open('C:\\Users\\Vinícius\\Documents\\UFPE\\Coding\\Python\\Dota\\dictID\\players.json', 'w') as writeFile:
        json.dump(data, writeFile, indent = 4, sort_keys = True)

def listPlayer(name):
    fileToJson = {}
    with open(jsonDirectory) as loadFile:
        data = json.load(loadFile)
    for x in range (0, len(data['players'])):
        if (data['players'][x]['Name'] == name):
            print (name + "'s ID is " + str(data['players'][x]['ID']))
            break
        else:
            if (len(data['players']) - x == 1):
                print("This player is not in our database")
