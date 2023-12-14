import os
import tweepy
import pymongo
from auth import api

TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
TWITTER_API_SECRET_KEY = os.getenv('TWITTER_API_SECRET_KEY')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

mongo_url = "mongodb://localhost:27017/"

def save_tweets_to_mongo(tweets, collection):
    try:
        mongo_client = pymongo.MongoClient(mongo_url)
        db = mongo_client.get_database('twitter_data')
        collection = db.get_collection(collection)
        for tweet in tweets:
            collection.insert_one(tweet._json)
        print('Tweets saved successfully to MongoDB')
    except Exception as e:
        print('Error: ', e)

def fetch_tweets(hashtag):
    try:
        tweets = tweepy.Cursor(api.search_tweets, q=hashtag, lang='en').items(100)
        return tweets
    except Exception as e:
        print('Error: ', e)

def main():
    hashtag = "#hashtag"
    tweets = fetch_tweets(hashtag)
    save_tweets_to_mongo(tweets, 'tweets')

if __name__ == '__main__':
    main()