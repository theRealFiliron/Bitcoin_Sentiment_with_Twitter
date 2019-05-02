import tweepy
import csv
import sys
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re

####input your credentials here
consumer_key = 'CEfahH2mXpbxu11PXoH4pHQ7R'
consumer_secret = 'ppCoXS2qrtIGiuA8giLeHQUcDso43oIUAzzo1yKS8XrsqrsbQA'
access_token = '821907928626167810-iXle89bPqozxkC6q2DOK6btJzNSwbQe'
access_token_secret = 'Ok3qSlQxvGBVYn8B3Fqk3p2omkJkopSqXijohfvHjh4cq'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# Open/Create a file to append data
file = open('tweets.txt', 'w+')

tweet_num = 3500

for tweet in tweepy.Cursor(api.search,q="#Bitcoin",count=100,
                           lang="en",
                           since="2019-04-21").items(tweet_num):
    # print (tweet.text)
    file.write(tweet.text)

file.close()

# Now, the sentiment analysis part

file = open(sys.argv[1], 'r')

text = file.readlines()[0]

# Clean the data

text = re.sub('@[^ ]*', '', text)
text = re.sub('#[^ ]*', '', text)
text = re.sub('http[^ ]', '', text)
text = re.sub('\s', ' ', text)
text = re.sub('\n', ' ', text)
text = re.sub('RT', '', text)

# sed 's/@[^ ]*//g' | sed 's/http[^ ]*//g' | sed 's/#[^ ]*//g' | sed 's/  */ /g' | sed 's/[^[:print:]t]//g' | tr -d '\n' > cleanTweet.txt

file.close()

analyser = SentimentIntensityAnalyzer()

file = open('sentimentTracker.txt', 'a')

file.write(sys.argv[1])
file.write(', ')
file.write(str(tweet_num))
file.write(', ')

def sentiment_analyzer_scores(s):
        return analyser.polarity_scores(s)

score = sentiment_analyzer_scores(text)

file.write(str(score))
file.write('\n')
print(str(score))

file.close()
