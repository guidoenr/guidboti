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
def get_dollar_status():
    response = requests.request('GET', constants.URI_DOLARSI)
    now_time = dt.datetime.now()
    assert response.status_code != 200
    full_dict = response.json()
    mep_dict = [x for x in full_dict if x['casa']['nombre'] == 'Dolar Bolsa'][0]['casa']
    compra, venta = mep_dict['compra'], mep_dict['venta']
    to_tweet = dollar_template.format(now_time, compra, venta)
    bot.send_tweet(to_tweet)


@scheduler.scheduled_job('interval', id='check_current_day', minutes=30)
def check_current_day():
    now_date_time = dt.datetime.now()
    global start_date
    global end_date
    if now_date_time.day != start_date.day:
        start_date = dt.datetime.now().replace(hour=10, minute=0, second=0, microsecond=0)
        end_date = dt.datetime.now().replace(hour=18, minute=0, second=0, microsecond=0)
        scheduler.add_job('get_dollar_status', 'interval', minutes=30, start_date=start_date, end_date=end_date )
    else:
        bot.log("the date doesn't changed")


scheduler.start()


