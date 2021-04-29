import os
import tweepy
import datetime
import pandas as pd

# Change working directory
os.chdir(r"C:\Users\niklm\PycharmProjects\Twitter")
cwd = os.getcwd()

# Twitter credentials
APIkey = "YMvDElA0XtM1Pb4Ip0ea1xBFR"
APIsecretKey = "0XhPUQipkcwvJnStn6KxKhEiunGTP9KI4Ou7JzZ8BCOX33jVW5"
accessToken = "1237052598286528513-tnD0D0WlM6o1F8YgK2qJ5ktzbIdrbG"
accessTokenSecret = "OXu388xkmTljxjGrsyDHJoBhgRsKndoDJ8ylOL2nopAgb"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(APIkey, APIsecretKey)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# defining search words
search_words = ["#covid19"]

# setting datetime
startDate = datetime.datetime(2021, 4, 27, 0, 0, 0)
endDate =   datetime.datetime(2021, 4, 28, 0, 0, 0)

# create empty data frame
tweets_df = pd.DataFrame(columns=['ID', 'Tweet Datetime', 'UserID', 'UserName', 'retweet_count', 'Tweet Text', 'language'])

# function for adding tweets to data frame
def process_tweets(tweet, tweets_df):
    for i in tweet:
        newTweet = [i.id_str, str(i.created_at), i.user.id, i.user.name, i.retweet_count, i.text, i.lang]
        tweets_df.loc[len(tweets_df)] = newTweet
    return

# loop for iterating trough tweets (limited to 15 per batch)
last_id = None
tweet = True
while tweet != None:
    tweet = api.search(q = search_words, since=startDate, until = endDate, max_id=last_id)
    process_tweets(tweet, tweets_df)
    if len(tweet) > 0:
        last_id = tweet[-1]._json['id']-1 # we subtract one to not have the same again.
    else:
        tweet = None

# export CSV
now = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
path = cwd + f"/output/covid_{now}.csv"
tweets_df.to_csv(path, index = False)
