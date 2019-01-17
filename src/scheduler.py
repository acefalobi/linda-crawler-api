import subprocess

import schedule
import time


def job():
    subprocess.run(['python', 'manage.py', 'runcrons'])


subprocess.run(['python', 'manage.py', 'runcrons'])
schedule.every(5).minutes.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
