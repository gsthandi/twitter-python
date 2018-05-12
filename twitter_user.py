# With a User object, find out things like how many followers an account has, who they are following, and more
import tweepy
from tweepy import OAuthHandler



CONSUMER_KEY = '""" CONSUMER_KEY (API KEY) FROM TWITTER """'
CONSUMER_SECRET = '""" CONSUMER_SECRET (API SECRET) FROM TWITTER """'
OAUTH_TOKEN = '""" OAUTH ACCESS TOKEN FROM TWITTER """'
OAUTH_TOKEN_SECRET = '""" OAUTH ACCESS SECRET FROM TWITTER """'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

user = api.get_user('@BarackObama')

print(user.screen_name)
print(user.followers_count)

for friend in user.friends():
    print(friend.screen_name)
    print(friend.followers_count)
    