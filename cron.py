from apscheduler.schedulers.background import BlockingScheduler
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
    # requests.post(...)
    print(datetime.now())

scheduler.add_job(execute, 'interval', minutes=1)

scheduler.start()
