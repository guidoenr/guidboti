import os
import tweepy as tweepy
import logging

logging.basicConfig(filename='status.log',
                    filemode='a',
                    format='[%(levelname)s] %(asctime)s: %(message)s',
                    level=logging.DEBUG)
logging.getLogger('apsscheduler')

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_KEY = os.environ['ACCESS_KEY']
ACCESS_SECRET = os.environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


def send_tweet(message):
    api.update_status(message)
    logging.info("twitted, @guidboti: {}".format(message))


def send_dm(message, user):
    api.send_direct_message(user, message)
    logging.warning("dm sent to @{}: {} ".format(user, message))


def log(message):
    logging.info(message)

