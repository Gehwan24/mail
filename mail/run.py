# -*- coding:utf-8 -*-
import logging
import subprocess
from time import gmtime, strftime
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

def clear():
   command = "python -m clear.py"
   subprocess.call(command.split())

def once():
   command = "python -m once.py"
   subprocess.call(command.split())

def main():
   command = "python -m main.py"
   subprocess.call(command.split())

if __name__ == "__main__":
   logging.basicConfig(level=logging.INFO)
   sched = BlockingScheduler()
   sched.add_job(clear, 'cron', hour="0", minute="30")
   sched.add_job(once, 'cron', hour="17", minute="20")
   sched.add_job(main, 'cron', hour="8-23", minute="59")
   sched.start()
   
  
