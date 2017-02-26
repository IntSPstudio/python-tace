#|==============================================================|#
# Made by IntSPstudio
# TaCe
# Thank you for using this software!
# Version: 0.0.1.20170226
# ID: 980003004
#
# Twitter: @IntSPstudio
#|==============================================================|#

#IMPORT
import it8c
import sys
import datetime
import engine
#START
if __name__ == "__main__":
	#TIMING
	backupStartTime = datetime.datetime.now()
	#VISUAL
	bgdLine = it8c.vslTerminalLine(0,"")
	#SETTINGS
	searchKeywordsID ="1"
	userTweetsEventID ="2"
	userGroupTweetsEventID ="3"
	#INPUT
	scrFile = sys.argv[0]
	scrRuleTest = len(sys.argv)
	scrRuleMode =0
	if scrRuleTest > 1:
		#ARG 1
		scrArg1 = str(sys.argv[1])
		scrRuleMode =1
		if scrRuleTest > 2:
			#ARG 2
			scrArg2 = str(sys.argv[2])
			scrRuleMode =2
			if scrRuleTest > 3:
				#ARG 3
				scrArg3 = str(sys.argv[3])
				scrRuleMode =3
	print(bgdLine)
	if scrRuleMode == 0:
		print("Input mode and argument(s)")
	else:
		if scrRuleMode > 1:
			#SEARCH KEYWORDS
			if scrArg1 == searchKeywordsID:
				checka = it8c.lettersdigits(scrArg2,"")
				if checka !="":
					engine.searchKeywordsBasic(scrArg2)
				else:
					print("Invalid keyword")
			#GET LATEST TWEETS BY USER
			elif scrArg1 == userTweetsEventID:
				checka = it8c.lettersdigits(scrArg2,"")
				if checka !="":
					print("Getting user "+ scrArg2 +"'s tweets:")
					userArrayContent = engine.getUserTweetHistoryBasic(scrArg2)
				else:
					print("Invalid user name")
			#GET LATEST TWEETS BY USER GROUP
			elif scrArg1 == userGroupTweetsEventID:
				if it8c.fileTextExists(scrArg2) == 1:
					userGroupList = it8c.fileReadText(scrArg2)
					userGroupListLength = len(userGroupList)
					for x in range(0,2):
						if x == 0:
							print("Users:")
						if x == 1:
							print(bgdLine)
							print("Getting tweets from:")
						for y in range(0,userGroupListLength):
							print(str(y +1) +": "+ str(userGroupList[y]))
							if x == 1:
								userArrayContent = engine.getUserTweetHistoryBasic(str(userGroupList[y]))
				else:
					print("File doesn't exists")
			else:
				print("Invalid event id")
		else:
			print("No arguments")
	#TIMING
	backupStopTime = datetime.datetime.now()
	backupDuration = backupStopTime - backupStartTime
	print(bgdLine)
	print("Time used: "+ str(backupDuration))