# Owner: Vinícius Aguiar de Oliveira
# Program I'm coding to learn the dota2api and maybe use it afterwards as an opening to start on the e-sports scence, you never know.

##################IMPORTS#####################
import json
##############################################

###############GLOBAL VARIABLES###############

##############################################

def findFile(name, path):
	for root, dirs, files in os.walk(path):
		if name in files:
			return True

def jsonLoadFile(jsonDirectory):
	with open(jsonDirectory) as loadFile:
		data = json.load(loadFile)
	loadFile.close()
	return data

def jsonWriteFile(jsonDirectory, data):
    with open(jsonDirectory, 'w') as writeFile:
        json.dump(data, writeFile, indent = 4, sort_keys = True)
    writeFile.close

def updateAdminFile(adminDirectory, content):
	with open(adminDirector, 'a') as writeFile:
		writeFile.write(content)
	writeFile.close

def optionOneWrite(name, content, fileDirectory, writer):
	with open(fileDirectory + name + ".txt", writer) as toCreate:
		toCreate.write(content)
	toCreate.close()
