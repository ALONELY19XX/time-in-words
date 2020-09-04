#! /usr/bin/env python3

import re

from helpers.timestrings import *
from helpers.timefunc import *

def time_in_words(timestr, use_minutes=False):
   """
   Transform given time string argument into phrase.
   [!] --> expected time string format: 'HH:MM'
   """

   # check if argumant has valid format and hours/minutes range
   if not re.match(r'^\d{2}:\d{2}$', timestr): 
      raise ValueError('[!] Argument doesn\'t match required time string format "HH:MM"')

   # split time string and extract hours and minutes
   hours, minutes = map(int, timestr.split(':'))

   # check if hours/minutes are within valid range
   if not (0 <= hours and hours <= 23 and 0 <= minutes and minutes <= 59):
      raise ValueError('[!] Hours/Minutes range invalid. Make Sure that hours in range [0...24] and minutes in range [0...59]')

   # CASE: full hour
   if minutes == 0:
     return f'{get_hours(hours)} o\'clock'
   # CASE: before half hour
   elif minutes < 30:
      # CASE: quarter passed
      if minutes == 15:
         return f'quarter past {get_hours(hours)}'
      # CASE: non-quarter passed
      else:
         return f'{get_minutes(minutes)}{append_minutes(minutes, use_minutes)} past {get_hours(hours)}'
   # CASE: half hour
   elif minutes == 30:
      return f'half past {get_hours(hours)}'
   # CASE: past half hour
   else:
      # CASE: quarter to full hour
      if minutes == 45:
         return f'quarter to {get_hours(hours+1)}'
      # CASE: non-quarter before full hour
      else:
         return f'{get_minutes(minutes)}{append_minutes(60-minutes, use_minutes)} to {get_hours(hours+1)}'
   

print(time_in_words('00:00', True))
print(time_in_words('01:00', True))
print(time_in_words('12:01', True))
print(time_in_words('14:15', True))
print(time_in_words('15:30', True))
print(time_in_words('15:36', True))
print(time_in_words('16:45', True))
print(time_in_words('16:50', True))
print(time_in_words('16:59', True))