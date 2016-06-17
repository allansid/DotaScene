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
    loadFile.close()
    data['players'].append(jsonToFile)
    with open(jsonDirectory, 'w') as writeFile:
        json.dump(data, writeFile, indent = 4, sort_keys = True)
    writeFile.close()
    print("The player " + name + " with ID " + str(ID) + " has been saved to our database")

def deletePlayer(name):
    with open(jsonDirectory) as loadFile:
        data = json.load(loadFile)
    loadFile.close()
    for x in range (0, len(data['players'])):
        if (data['players'][x]['Name'] == name):
            del data['players'][x]
            print("Player " + name + " has been deleted")
            break
        elif (len(data['players']) - x == 1):
            print("This player is not in our database, you are good to go")
    with open(jsonDirectory, 'w') as writeFile:
        json.dump(data, writeFile, indent = 4, sort_keys = True)
    writeFile.close

def listPlayer(name):
    with open(jsonDirectory) as loadFile:
        data = json.load(loadFile)
    loadFile.close()
    for x in range (0, len(data['players'])):
        if (data['players'][x]['Name'] == name):
            print (name + "'s ID is " + str(data['players'][x]['ID']))
            break
        elif (len(data['players']) - x == 1):
            print("This player is not in our database")

def existsPlayer(ID):
    with open(jsonDirectory) as loadFile:
        data = json.load(loadFile)
    loadFile.close()
    for x in range(0, len(data['players'])):
        if (data['players'][x]['ID'] == ID):
            return True
        elif (len(data['players']) - x == 1):
            return False

def getName(ID):
    with open(jsonDirectory) as loadFile:
        data = json.load(loadFile)
    loadFile.close()
    for x in range(0, len(data['players'])):
        if (data['players'][x]['ID'] == ID):
            return data['players'][x]['Name']
        elif (len(data['players']) - x == 1):
            return None
