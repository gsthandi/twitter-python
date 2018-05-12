# How many unique words are used in a text
import json 
import tweepy
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable


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
            
            
for label, data in (('Text', status_texts),
                        ('Screen Name', screen_names),
                            ('Word', words)):
    table = PrettyTable(field_names=[label, 'Count'])
    counter = Counter(data)
    [table.add.row(entry) for entry in counter.most_common()[:10]]
    table.align[label], table.align['Count'] = '1', 'r' # align the columns
    print(table)
    
def get_lexical_diversity(items):
    return 1.0*len(set(items))/len(items) # change items to a set to ensure all items are unique
    
def get_average_words(tweets):
    total_words = sum([len(tweet.split()) for tweet in tweets])
    return 1.0*total_words/len(tweets)
    
print("Average words: {0}".format(get_average_words(status_texts)))
print("Word Diversity: {0}".format((get_lexical_diversity(words))))
print("Screen Name Diversity: {0}".format(get_lexical_diversity(screen_names)))
print("Hashtag Diversity: {0}".format(get_lexical_diversity(hashtags)))

"""we can see the output so we have an average words there of 17.74 in each
harvested tweet returned from the set. That tells us that tweets are quite
chatty. A word diversity of 0.36 tells us that 36% of the words used in harvested
tweets were unique. This means that the discussion around the topic was moderately rich
and diverse. A screen name diversity of 0.75 tells us that 75% of the screen
names used in the harvested tweets were unique so this indicates there is a wide
variety of unique user names included in harvest tweets. Hashtag diversity of 1
tells us that all of the hashtags were unique. In this case it looks as though
very few hashtags or possibly just one was added which is why we're getting
that result
"""