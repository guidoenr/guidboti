#import bot
import constants
import requests
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler(timezone='UTC-3')
INTERVAL = constants.INTERVAL_1_HOURS


# returns compra-venta, in that order
@scheduler.scheduled_job('cron', day_of_week='mon-tue-wed-thu-fri')
def get_dollar_status():
    response = requests.request('GET', constants.URI_DOLARSI)
    if response.status_code != 200:
        return "-1", "-1"
    full_dict = response.json()
    mep_dict = [x for x in full_dict if x['casa']['nombre'] == 'Dolar Bolsa'][0]['casa']
    return mep_dict['compra'], mep_dict['venta']


