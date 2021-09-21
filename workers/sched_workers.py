from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.combining import AndTrigger
import datetime as dt
import worker_dollar as wd

import bot

blockingScheduler = BlockingScheduler(timezone='America/Argentina/Buenos_Aires')

trigger_interval = IntervalTrigger(seconds=20, start_date=wd.DATE_START, end_date=wd.DATE_END)
trigger_cron = CronTrigger(day_of_week='mon,tue,wed')
trigger_combined = AndTrigger([trigger_interval, trigger_cron])


def test_fun():
    bot.log("TEST_FUNC")




