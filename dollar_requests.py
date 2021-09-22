import bot
import constants
import requests
from datetime import datetime as dt

dollar_template = """
Dollar MEP status at {}
Compra: {}
Venta: {}
@guidoenr
"""


def post_dollar_status():
    response = requests.request('GET', constants.URI_DOLARSI)
    assert response.status_code == 200
    full_dict = response.json()
    to_tweet = tweet_format(full_dict)
    bot.send_tweet(to_tweet)


# returns compra-venta values, in that order
def tweet_format(dict_response):
    mep_dict = [x for x in dict_response if x['casa']['nombre'] == 'Dolar Bolsa'][0]['casa']
    compra, venta = mep_dict['compra'], mep_dict['venta']
    hour, minute = dt.now().hour, dt.now().minute
    current_time = "{}:{}".format(hour, minute)
    to_tweet = dollar_template.format(current_time, compra, venta)
    return to_tweet

