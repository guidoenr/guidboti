import bot
import datetime as dt
import constants
import requests
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler(timezone='America/Argentina/Buenos_Aires')
start_date = dt.datetime.now().replace(hour=20, minute=13, second=0, microsecond=0)
end_date = dt.datetime.now().replace(hour=20, minute=20, second=0, microsecond=0)


# returns compra-venta, in that order
# @scheduler.scheduled_job('interval', minutes=30, start_date=start_date, end_date=end_date)
def get_dollar_status():
    response = requests.request('GET', constants.URI_DOLARSI)
    if response.status_code != 200:
        return "-1", "-1"
    full_dict = response.json()
    mep_dict = [x for x in full_dict if x['casa']['nombre'] == 'Dolar Bolsa'][0]['casa']
    return mep_dict['compra'], mep_dict['venta']


@scheduler.scheduled_job('interval', seconds=67, start_date=start_date, end_date=end_date)
def test_to_print():
    n = dt.datetime.now().minute
    bot.send_tweet("[scheduler_test]: a ver q onda: " + str(n))


scheduler.start()
