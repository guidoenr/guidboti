import bot
import constants
import requests
import glogger
from datetime import datetime as dt

dollar_template = """
Dollar MEP status changed at {}
Compra: {}
Venta: {}
"""


def post_dollar_status():
    response = requests.request('GET', constants.URI_DOLARSI)
    assert response.status_code == 200
    full_dict = response.json()
    mep_dict = [x for x in full_dict if x['casa']['nombre'] == 'Dolar Bolsa'][0]['casa']
    compra, venta = mep_dict['compra'], mep_dict['venta']
    if check_dollar_value(compra, venta):
        update_dollar_value(compra, venta)
        hour, minute = dt.now().hour, dt.now().minute
        current_time = "{}:{}".format(hour, minute)
        to_tweet = dollar_template.format(current_time, compra, venta)
        bot.send_tweet(to_tweet)
    else:
        glogger.log_warning("the dollar value doesn't changed")


def check_dollar_value(new_compra, new_venta):
    stats_file = open(file='values.dat', mode='r')
    old_compra = stats_file.readline()
    old_venta = stats_file.readline()
    stats_file.close()
    return True if (str(new_compra), str(new_venta)) != (old_compra.replace('\n', ''), old_venta) else False


def update_dollar_value(new_compra, new_venta):
    with open(file='values.dat', mode='w') as new_file:
        new_file.write(str(new_compra) + '\n')
        new_file.write(str(new_venta))

