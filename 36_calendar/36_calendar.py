#!/usr/bin/python3
import calendar
import time

def get_year():
  return time.localtime().tm_year
  
def get_month():
  return time.localtime().tm_mon 

def print_current_time():
  localtime = time.asctime( time.localtime(time.time()) )
  print("Local time: {}\n".format(localtime))

def print_current_month(year, month):
  this_month_calendar = calendar.month(year, month)
  print(this_month_calendar)

this_year = get_year()
this_month = get_month()

print_current_time()
print_current_month(this_year, this_month)