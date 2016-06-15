# Owner: Vinícius Aguiar de Oliveira
# Program I'm coding to learn the dota2api and maybe use it afterwards as an opening to start on the e-sports scence, you never know.

##################IMPORTS#####################
import json
##############################################

################GLOBAL VARIABLES################
dictDirectory = "C:\\Users\\Vinícius\\Documents\\UFPE\\Coding\\Python\\Dota\\dictID\\"
################################################

def optionTwo():
    print ("Type 1 to search an ID")
    print ("Type 2 to add a ID to the list")
    print ("Type 3 to remove a saved AD")
    option = int(input())

    if (option == 1):
        print ("What's the name of the person you want to check?")
        name = input()
        fileToJson = {}
        with open('C:\\Users\\Vinícius\\Documents\\UFPE\\Coding\\Python\\Dota\\dictID\\ID.json') as loadFile:
            data = json.load(loadFile)
        print (name + "'s ID is " + str(data[name]))


    elif (option == 2):
        print ("What is the name of the person you want to add?")
        name = input()
        print ("What is his/her ID?")
        ID = int(input())

        jsonToFile = {name: ID}
        with open('C:\\Users\\Vinícius\\Documents\\UFPE\\Coding\\Python\\Dota\\dictID\\ID.json') as loadFile:
            data = json.load(loadFile)
        data.update(jsonToFile)
        with open('C:\\Users\\Vinícius\\Documents\\UFPE\\Coding\\Python\\Dota\\dictID\\ID.json', 'w') as writeFile:
            json.dump(data, writeFile)

    elif (option == 3):
        print ("What is the name of the person you want out of the list?")
        name = input()

        with open('C:\\Users\\Vinícius\\Documents\\UFPE\\Coding\\Python\\Dota\\dictID\\ID.json') as loadFile:
            data = json.load(loadFile)
        del data[name]
        with open('C:\\Users\\Vinícius\\Documents\\UFPE\\Coding\\Python\\Dota\\dictID\\ID.json', 'w') as writeFile:
            json.dump(data, writeFile)
