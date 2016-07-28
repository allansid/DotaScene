# coding: utf-8
# Owner: Vinícius Aguiar de Oliveira
# Program I'm coding to learn the dota2api and maybe use it afterwards as an opening to start on the e-sports scence, you never know.

##################IMPORTS#####################
import dota2api
import greetings
import o1
import o2
import os
##############################################

################GLOBAL VARIABLES################
fileDirectory = '../txtResults/'
apiKey = os.environ['dota2_api_key']
################################################

def main():
	myAccountID = greetings.login()
	while (1):
		option = greetings.greetings()
		if (option == 0):
			break
		elif (option == 1):
			o1.optionOne(api, myAccountID, fileDirectory)
		elif (option == 2):
			o2.optionTwo(myAccountID)
		elif (option != 0 or option != 1 or option != 2):
			print("Wrong option, try again\n")

##########################RUNNER##########################
api = dota2api.Initialise(apiKey)
main()
##########################################################
