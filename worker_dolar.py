#import bot
import datetime
import constants
import requests
from datetime import datetime as dt

INTERVAL = constants.INTERVAL_1_HOURS


# returns compra-venta, in that order
def get_dollar_status():
    response = requests.request('GET', constants.URI_DOLARSI)
    if response.status_code != 200:
        return "-1", "-1"
    full_dict = response.json()
    mep_dict = [x for x in full_dict if x['casa']['nombre'] == 'Dolar Bolsa'][0]['casa']
    return mep_dict['compra'], mep_dict['venta']

print(datetime.datetime.now())
