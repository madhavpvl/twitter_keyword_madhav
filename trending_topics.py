import tweepy
import pymongo
import time
import os
from auth import api

TWITTER_API_KEY = os.getenv= "cahicoWKXdrcx0kMcWmrkzGgY"
TWITTER_API_SECRET_KEY = os.getenv = "Mam8ZoSVhsU3L6lqJ5S0EhK4vbyj2BWYMELgSNDMKR2cADxlpr"
TWITTER_ACCESS_TOKEN = os.getenv = "1675423387-Kp0NxfF4jquYovDmppptmbtU4HW85VXq0L9i7JF"
TWITTER_ACCESS_TOKEN_SECRET = "3CF0Vr66XZrablKqzNIcEAs78trdSiooqUWd0ATZ25lt7"

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

db_url = "mongodb://madhav:madhav@localhost:27017/?authMechanism=DEFAULT"
client = pymongo.MongoClient(db_url)
db = client.trending_topics

def get_trending_topics(location_id):
    trending_data = api.trends_place(location_id)
    trending_topics = trending_data[0]["trends"]

    return trending_topics

def store_trending_topics(trending_topics):
    for topic in trending_topics:
        topic_id = topic["id"]
        topic_name = topic["name"]

        if not db.topics.find_one({"id": topic_id}):
            db.topics.insert_one({"id": topic_id, "name": topic_name})

location_id = 1
while True:
    try:
        trending_topics = get_trending_topics(location_id)
        store_trending_topics(trending_topics)

        print("Trending topics have been retrieved and stored successfully.")

        time.sleep(60)
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(60)