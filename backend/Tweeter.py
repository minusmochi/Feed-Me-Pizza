from requests_oauthlib import OAuth1Session
import requests
from requests_oauthlib import OAuth1
import os
from dotenv import load_dotenv

load_dotenv()

class Tweeter:
    url = "https://api.twitter.com/1.1/statuses/update.json?status=This is from python!"
    def tweet(self):
        consumerKey = os.getenv("consumerKey")
        consumerSecret = os.getenv("consumerSecret")
        accessKey = os.getenv("accessKey")
        secret = os.getenv("secret")

        oauth = OAuth1(consumerKey,
                   client_secret=consumerSecret,
                   resource_owner_key=accessKey,
                   resource_owner_secret=secret)
        r = requests.post(url=self.url, auth=oauth)

        print(r)

t = Tweeter()

t.tweet()