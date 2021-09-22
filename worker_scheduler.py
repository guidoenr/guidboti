from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger
import dollar_requests as wd
import glogger
from exceptions import exceptions

scheduler = BlockingScheduler(timezone='America/Argentina/Buenos_Aires')
trigger_interval = IntervalTrigger(minutes=10)


def start():
    try:
        scheduler.add_job(func=wd.post_dollar_status, trigger=trigger_interval)
        scheduler.start()
        glogger.log_ok("scheduler started, jobs: {}".format(scheduler.get_jobs()))
    except exceptions.SchedulerException:
        glogger.log_error("scheduler FAILED, please check the logs")


# trigger_cron_start = CronTrigger(day_of_week='mon,tue,wed,thu,fri', hour=11, minute=30)
# trigger_cron_stop = CronTrigger(day_of_week='mon,tue,wed,thu,fri', hour=18, minute=0)


# def start_interval():
#    scheduler.add_job(id='tweet_dollar', func=wd.post_dollar_status, trigger=trigger_interval)


# def stop_interval():
#    scheduler.remove_job(job_id='tweet_dollar')


start()
