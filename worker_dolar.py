import datetime
import bot
import datetime as dt
import constants
import requests
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler(timezone='America/Argentina/Buenos_Aires')
start_date = dt.datetime.now().replace(hour=11, minute=0, second=0, microsecond=0)
end_date = dt.datetime.now().replace(hour=18, minute=0, second=0, microsecond=0)

dollar_template = """
[DOLLAR_MEP_STATUS] at {}
Compra: {}
Venta: {}
"""


# returns compra-venta, in that order
@scheduler.scheduled_job('interval', minutes=30, start_date=start_date, end_date=end_date)
def get_dollar_status():
    response = requests.request('GET', constants.URI_DOLARSI)
    now_time = datetime.datetime.now()
    assert response.status_code != 200
    full_dict = response.json()
    mep_dict = [x for x in full_dict if x['casa']['nombre'] == 'Dolar Bolsa'][0]['casa']
    compra, venta = mep_dict['compra'], mep_dict['venta']
    to_tweet = dollar_template.format(now_time, compra, venta)
    bot.send_tweet(to_tweet)


scheduler.start()


