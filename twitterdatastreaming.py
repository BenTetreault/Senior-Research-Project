#Twitter Streaming
#Source: http://socialmedia-class.org/twittertutorial.html

# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API
ACCESS_TOKEN = '922599141368385537-8BGkHyp4drA6M46X0KMTJxhVNFzzXDf'
ACCESS_SECRET = 'tWBA0RSe2UmskqiLLUmwoiiYpmeUAnzSHlpTAG3ue8E1f'
CONSUMER_KEY = 'z29pZvL7aoz5a5Cd7mKuAKuRQ'
CONSUMER_SECRET = 'PFXGS3wgWkN1BnwPdzTncJY0rI57ntQRtaeB0TxFiCKZrl26y7'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.sample()

# Print each tweet in the stream to the screen
# Here we set it to stop after getting 1000 tweets.
# You don't have to set it to stop, but can continue running
# the Twitter API to collect data for days or even longer.
tweet_count = 2
for tweet in iterator:
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    print(json.dumps(tweet))

    # The command below will do pretty printing for JSON data, try it out
    ##print(json.dumps(tweet, indent=4))

    if tweet_count <= 0:
        break