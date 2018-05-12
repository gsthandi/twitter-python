import json 
import tweepy
from tweepy import OAuthHandler


CONSUMER_KEY = '""" CONSUMER_KEY (API KEY) FROM TWITTER """'
CONSUMER_SECRET = '""" CONSUMER_SECRET (API SECRET) FROM TWITTER """'
OAUTH_TOKEN = '""" OAUTH ACCESS TOKEN FROM TWITTER """'
OAUTH_TOKEN_SECRET = '""" OAUTH ACCESS SECRET FROM TWITTER """'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

count = 10
query = 'Dublin'

# Get all status
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

for result in results:
    print(json.dumps(result._json, indent=2))
    
for status in results:
    print(status.text.encode('utf-8'))
    print(status.user.id)
    print(status.user.screen_name)
    print(status.user.profile_image_url_https)
    print(status.user.followers_count)
    print(status.place)