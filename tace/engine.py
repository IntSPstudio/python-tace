#|==============================================================|#
# Made by IntSPstudio
# TaCe
# Thank you for using this software!
# ID: 980003004
#
# Twitter: @IntSPstudio
#|==============================================================|#

#IMPORT
import tweepy
import it8c
import authentication
import string
import os
#SETTINGS
dataFolder ="data"
#AUTHENTICATION
consumerKey = authentication.consumerKey
consumerSecret = authentication.consumerSecret
accessToken = authentication.accessToken
accessTokenSecret = authentication.accessTokenSecret
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)
#USER TWEET HISTORY 1
def getUserTweetRawDataHistory(screen_name):
	alltweets = []
	new_tweets = api.user_timeline(screen_name,count=200)
	alltweets.extend(new_tweets)
	oldest = alltweets[-1].id - 1
	while len(new_tweets) > 0:
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		alltweets.extend(new_tweets)
		oldest = alltweets[-1].id - 1
		print(str(len(alltweets)) +" tweets downloaded")
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
	return outtweets
#USER TWEET HISTORY 2
def getUserTweetHistoryBasic(userName):
	userContent = getUserTweetRawDataHistory(userName)
	userContentHeight = len(userContent)
	for i in range(0,userContentHeight):
		pointa = str(userContent[i][2])
		pointaLength = len(pointa)
		pointb =""
		for j in range(2, pointaLength -1):
			pointb = pointb + str(pointa[j])
		userContent[i][2] = pointb
	userNameBasic = str.lower(it8c.lettersdigits(userName,""))
	if not os.path.exists(dataFolder):
		os.makedirs(dataFolder)
	userFileName = dataFolder +"/tweethistory_"+ userNameBasic +".csv"
	it8c.csvWriteFile(userContent,userFileName,";",0)
	return userContent
#SEARCH KEYWORDS
def searchKeywordsBasic(keyWord):
	public_tweets = api.search(keyWord)
	cacheArray = [tweet.text.encode("utf-8") for tweet in public_tweets]
	cacheArrayLength = len(cacheArray)
	print(str(cacheArrayLength) +" tweets downloaded")
	outputArray = it8c.dataCreateList(cacheArrayLength,"")
	for i in range(cacheArrayLength):
		pointa = str(cacheArray[i])
		pointaLength = len(pointa)
		pointb =""
		for j in range(2, pointaLength -1):
			pointb = pointb + str(pointa[j])
		outputArray[i] = str(pointb)
	keywordNameBasic = str.lower(it8c.lettersdigits(keyWord,""))
	if not os.path.exists(dataFolder):
		os.makedirs(dataFolder)
	keywordFileName = dataFolder +"/keyword_"+ keywordNameBasic +".txt"
	it8c.fileWriteTextList(outputArray,keywordFileName)