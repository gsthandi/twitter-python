# Counting instances of attributes
import json 
import tweepy
from tweepy import OAuthHandler
from collections import Counter


CONSUMER_KEY = '""" CONSUMER_KEY (API KEY) FROM TWITTER """'
CONSUMER_SECRET = '""" CONSUMER_SECRET (API SECRET) FROM TWITTER """'
OAUTH_TOKEN = '""" OAUTH ACCESS TOKEN FROM TWITTER """'
OAUTH_TOKEN_SECRET = '""" OAUTH ACCESS SECRET FROM TWITTER """'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

count = 50
query = 'weather'

# Get all tweets for the search query 
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

status_texts = [status._json['text'] for status in results]

screen_names = [status._json['user']['screen_name']
                for status in results
                    for mention in status._json['entities']['user_mentions'] ]
        
hashtags = [hashtag['text']
            for status in results
                for hashtag in status._json['entities']['hashtags'] ]
                
words = [ word 
        for text in status_texts
            for word in text.split() ]
            
            
for entry in [screen_names, hashtags, words]:
    counter = Counter(entry)
    print(counter.most_common()[:10]) # the top 10 results


