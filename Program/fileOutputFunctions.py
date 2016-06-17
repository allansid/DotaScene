# Owner: Vinícius Aguiar de Oliveira
# Program I'm coding to learn the dota2api and maybe use it afterwards as an opening to start on the e-sports scence, you never know.

##################IMPORTS#####################
import jsonFunctions
import json
##############################################

###############GLOBAL VARIABLES###############

##############################################

def findFile(name, path):
	for root, dirs, files in os.walk(path):
		if name in files:
			return True

def createAccountFile(myAccountID, name, content, accountDirectory):
    with open(accountDirectory + name + "File.txt", "a") as createAccount:
        createAccount.write(content)
    jsonFunctions.addNewPlayer(name, myAccountID)

def jsonLoadFile(jsonDirectory):
    with open(jsonDirectory) as loadFile:
        data = json.load(loadFile)
    loadFile.close()
    return data

def jsonWriteFile(jsonDirectory):
    with open(jsonDirectory, 'w') as writeFile:
        json.dump(data, writeFile, indent = 4, sort_keys = True)
    writeFile.close
