import tweepy
import sqlite3

# replace these values with your own
consumer_key = "pl9TFy6tjBJr5jlNMlSv2HAxU"
consumer_secret = "dRqF0meswsyGyLFZVNDhbv2JSfzBtDjJgNLOlW2gg6rO4fC4yG"
access_token = "319775825-MTPmpV4V4ejn2TSwzQEyillq4bfrSZLPNChOiIYR"
access_token_secret = "MPMNFlIDzprnhW5c9YZu4Zj7qfMSxzoCXNFiZJnxVAZba"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Create a SQLite database connection
conn = sqlite3.connect('twitter_data.db')
c = conn.cursor()

# Create table if it does not exist
c.execute('''
    CREATE TABLE IF NOT EXISTS tweets (
        id_str TEXT PRIMARY KEY,
        created_at TIMESTAMP,
        text TEXT,
        user_name TEXT,
        user_location TEXT,
        user_description TEXT
    )
''')

# select the Twitter user you want to get tweets from
user = api.get_user('EU_Commission')

# iterate through their tweets (Twitter API only allows access to the user's most recent 3200 tweets)
for status in tweepy.Cursor(api.user_timeline, id=user.id).items():
    c.execute('''
        INSERT INTO tweets VALUES ("Security","Securitization", "Social Media", "Social Network", "Network", "Twitter")
    ''', (status.id_str, status.created_at, status.text, user.name, user.location, user.description))

# commit the transaction and close the connection
conn.commit()
conn.close()
