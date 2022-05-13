import tweepy
import json
from attrdict import AttrDict
import time
import datetime

with open("config.json", 'r') as f:
  config = AttrDict(json.load(f))

auth = tweepy.OAuthHandler(config.API_KEY, config.API_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

def search(write_file):
  while True:
    recent = None
    try:
      tweets = api.search_tweets(
        lang="ja",
        q=word, result_type="recent", count=100, max_id=recent)
    except tweepy.errors.TooManyRequests:
      print(f"too many requests {datetime.datetime.now()}")
      time.sleep(60 * 16)
      print("restart")
      continue

    if len(tweets) < 1:
      print("finish")
      return

    for tweet in tweets:
      #print(tweet.text)
      #print(tweet.created_at)
      #print(tweet.id)
      write_file.write(tweet.text + "\t" + str(tweet.created_at) + '\n')

    recent = tweet.id
    #print(tweet.created_at)
    #print(tweet.id)

for word in config.words:
  print(word)
  with open(f"{word}.txt", "w") as f:
    search(f)

