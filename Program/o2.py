# Owner: Vinícius Aguiar de Oliveira
# Program I'm coding to learn the dota2api and maybe use it afterwards as an opening to start on the e-sports scence, you never know.

##################IMPORTS#####################
import json
##############################################

################GLOBAL VARIABLES################
dictDirectory = "C:\\Users\\Vinícius\\Documents\\UFPE\\Coding\\Python\\Dota\\dictID\\"
################################################

def optionTwo():
    while (1):
        print ("\nType 1 to search an ID")
        print ("Type 2 to add a ID to the list")
        print ("Type 3 to remove a saved AD")
        print ("Type 0 to go back\n")
        option = int(input())
        if (option == 0):
            break

        elif (option == 1):
            print ("What's the name of the person you want to check?")
            name = input()
            fileToJson = {}
            with open('C:\\Users\\Vinícius\\Documents\\UFPE\\Coding\\Python\\Dota\\dictID\\players.json') as loadFile:
                data = json.load(loadFile)

            for x in range (0, len(data['players'])):
                if (data['players'][x]['Name'] == name):
                    print (name + "'s ID is " + str(data['players'][x]['ID']))
                    break
                else:
                    if (len(data['players']) - x == 1):
                        print("Name not found, try again")

        elif (option == 2):
            print ("What is the name of the person you want to add?")
            name = input()
            print ("What is his/her ID?")
            ID = int(input())
            jsonToFile = {'Name': name, 'ID': ID}
            with open('C:\\Users\\Vinícius\\Documents\\UFPE\\Coding\\Python\\Dota\\dictID\\players.json') as loadFile:
                data = json.load(loadFile)
            data['players'].append(jsonToFile)
            with open('C:\\Users\\Vinícius\\Documents\\UFPE\\Coding\\Python\\Dota\\dictID\\players.json', 'w') as writeFile:
                json.dump(data, writeFile, indent = 4, sort_keys = True)

        elif (option == 3):
            print ("What is the name of the person you want out of the list?")
            name = input()
            with open('C:\\Users\\Vinícius\\Documents\\UFPE\\Coding\\Python\\Dota\\dictID\\players.json') as loadFile:
                data = json.load(loadFile)
            for x in range (0, len(data['players'])):
                if (data['players'][x]['Name'] == name):
                    del data['players'][x]
                    print("Player " + name + "has been deleted")
                    break
            with open('C:\\Users\\Vinícius\\Documents\\UFPE\\Coding\\Python\\Dota\\dictID\\players.json', 'w') as writeFile:
                json.dump(data, writeFile, indent = 4, sort_keys = True)
