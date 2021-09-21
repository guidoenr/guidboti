from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.combining import AndTrigger
import datetime as dt
import worker_dollar as wd
import bot

scheduler = BlockingScheduler(timezone='America/Argentina/Buenos_Aires')

trigger_interval = IntervalTrigger(minutes=20)
trigger_cron = CronTrigger(day_of_week='mon,tue,wed,thu,fri')


def test_fun():
    bot.log("TEST_FUNC")


test_job = scheduler.add_job(test_fun, trigger=trigger_cron)
scheduler.start()







