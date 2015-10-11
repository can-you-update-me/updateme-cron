from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

import requests

scheduler = BlockingScheduler({
    'apscheduler.jobstores.default': {
        'type': 'memory'
    },
    'apscheduler.executors.default': {
        'class': 'apscheduler.executors.pool:ThreadPoolExecutor',
        'max_workers': '2'
    },
    'apscheduler.executors.processpool': {
        'type': 'processpool',
        'max_workers': '1'
    },
    'apscheduler.job_defaults.coalesce': 'false',
    'apscheduler.job_defaults.max_instances': '2',
    'apscheduler.timezone': 'UTC'
})


def execute():
    log('Cron job kicking off')
    response = requests.post('http://web:3000/time_to_update')
    if response.ok:
        log(
            'Cron job kicked off successfully: {} {}',
            response.status_code,
            response.reason
        )
    else:
        log(
            'Cron job failed to kick off: {} {}',
            response.status_code,
            response.reason
        )


def log(line, *args):
    print(datetime.now().isoformat(), line.format(*args))


scheduler.add_job(execute, 'interval', minutes=1)

log('Starting cron...')
scheduler.start()
