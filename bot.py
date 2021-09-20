import os, time
import tweepy as tweepy

from datetime import datetime, timedelta
from get_dolar_status import *

INTERVAL = constants.INTERVAL_1_HOURS
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_KEY = os.environ['ACCESS_KEY']
ACCESS_SECRET = os.environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


while True:
    arg_time = datetime.utcnow() - timedelta(hours=3)
    api.update_status("empty: scaled 1 dyno")
    time.sleep(INTERVAL)

