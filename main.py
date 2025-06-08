
import time
from datetime import datetime 
def get_current_time():
  return datetime.now().strftime("%I:%M %p)")

print(" current time is", get_current_time())

def set_alarm(alarm_time):
  print(f"Alarm set for {alarm_time}")
  while True:
    current_time = get_current_time()
    if current_time == alarm_time:
      print(f"alarm time it is now {alarm_time}.  wake up!")
      break
      time.sleep(60)

alarm_time = input("set alarmtime; example 06:00 AM : ")
set_alarm(alarm_time)
