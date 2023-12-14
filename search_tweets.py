from auth import api

# Replace 'YOUR_KEYWORD' with the keyword you want to search for
keyword = 'cat'

# Retrieve the first 100 tweets containing the keyword
tweets = api.search(q=keyword, tweet_mode='extended')

# Print the details of each tweet
for tweet in tweets:
    print('Username: ', tweet.user.screen_name)
    print('Tweet ID: ', tweet.id)
    print('Tweet Text: ', tweet.text)
    print('Created at: ', tweet.created_at)
    print('Retweets: ', tweet.retweet_count)
    print('Favorites: ', tweet.favorite_count)
    print('---')