import tweepy
import pandas as pd 
import json
from datetime import datetime
import s3fs

access_key = "90h6j1COS4whpoEPoWDHURxy6"
access_secret = "oOJNHlzimqhXflHwC5CUUr6yegECP3lLvsWCgp4OMkvPOxRXHr"
customer_key = "1698805986771779589-89muiuxyW7rCTFslE6rFjVIZ2VUEgT"
customer_secret = "JSDd8O583W3dkBpGkZlsKxhHYwPmexR0K8oyxWK5FWQCm"

#Twitter authentication
auth = tweepy.OAuthHandler(access_key, access_secret)
auth.set_access_token(customer_key, customer_secret)

#Creating an API object
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name="elon_musk", count=200, 
                           #retweets we dont want so false
                           include_rts=False,
                           tweet_mode="extended")


#looping through each individual tweet and extracting data from it
tweet_list = []
for tweet in tweets:
    text = tweet._json['full_text']
    refined_tweet = {"user": tweet.user.screen_name,
                     #from the above json file we can get the text of the tweet
                     'text': text,
                     #how many like the tweet
                     'favorite_count': tweet.favorite_count,
                     #how many retweeted the tweet
                     'retweet_count': tweet.retweet_count,
                     #when the tweet was created
                     'created_at': tweet.created_at
                     }
    tweet_list.append(refined_tweet)

df = pd.DataFrame(tweet_list)
df.to_csv("elon_musk_tweetsdata.csv", index=False)
