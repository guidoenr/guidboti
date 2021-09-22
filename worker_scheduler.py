from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger
import dollar_requests as wd

scheduler = BlockingScheduler(timezone='America/Argentina/Buenos_Aires')

trigger_interval = IntervalTrigger(minutes=15)
trigger_cron_start = CronTrigger(day_of_week='mon,tue,wed,thu,fri', hour=11, minute=30)
trigger_cron_stop = CronTrigger(day_of_week='mon,tue,wed,thu,fri', hour=18, minute=0)


def start_interval():
    scheduler.add_job(id='tweet_dollar', func=wd.post_dollar_status, trigger=trigger_interval)


def stop_interval():
    scheduler.remove_job(job_id='tweet_dollar')


job_start_interval = scheduler.add_job(start_interval, trigger=trigger_cron_start)
job_stop_interval = scheduler.add_job(stop_interval, trigger=trigger_cron_stop)
scheduler.start()
