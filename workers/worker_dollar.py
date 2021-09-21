import credentials
import bot
import constants
import requests
from datetime import datetime as dt

dollar_template = """
Dollar MEP status \n
Compra: {} \n
Venta: {}
"""

DATE_START = dt.now().replace(hour=16, minute=2, second=0, microsecond=0)
DATE_END = dt.now().replace(hour=18, minute=0, second=0, microsecond=0)


def post_dollar_status():
    response = requests.request('GET', constants.URI_DOLARSI)
    assert response.status_code == 200
    full_dict = response.json()
    to_tweet = tweet_format(full_dict)
    bot.log(to_tweet)# TODO here, tweet


# returns compra-venta values, in that order
def tweet_format(dict):
    mep_dict = [x for x in dict if x['casa']['nombre'] == 'Dolar Bolsa'][0]['casa']
    compra, venta = mep_dict['compra'], mep_dict['venta']
    to_tweet = dollar_template.format(compra, venta)
    return to_tweet
