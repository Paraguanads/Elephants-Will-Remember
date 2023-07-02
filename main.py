import os
from dotenv import load_dotenv
import tweepy
from mastodon import Mastodon

# Load environment variables from .env
load_dotenv()

# Twitter cfg
twitter_consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
twitter_consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
twitter_access_token = os.getenv("TWITTER_ACCESS_TOKEN")
twitter_access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Mastodon cfg
mastodon_base_url = os.getenv("MASTODON_BASE_URL")
mastodon_client_id = os.getenv("MASTODON_CLIENT_ID")
mastodon_client_secret = os.getenv("MASTODON_CLIENT_SECRET")
mastodon_access_token = os.getenv("MASTODON_ACCESS_TOKEN")

# Twitter auth
auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
auth.set_access_token(twitter_access_token, twitter_access_token_secret)
twitter_api = tweepy.API(auth)

# Mastodon auth
mastodon_api = Mastodon(
    client_id=mastodon_client_id,
    client_secret=mastodon_client_secret,
    access_token=mastodon_access_token,
    api_base_url=mastodon_base_url,
)

# Get the latest tweets
tweets = twitter_api.user_timeline(screen_name="your_username", count=10)  # Replace username with yours

# Send tweets to Mastodon
for tweet in tweets:
    status = f"{tweet.user.screen_name}: {tweet.text}"
    mastodon_api.toot(status)

print("Tweet correctly sent!")
