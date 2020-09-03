#! /usr/bin/env python3

from timestrings import *

def get_hours(hours):
   """
   Get AM/PM hours --> 1 => 1, 2 => 2, ..., 13 => 1, 14 => 2, ...
   """
   return hours if hours == 12 else hours % 12

def get_minutes(minutes):
   """
   Get minutes as string.
   If minutes < 30, then minutes as string is returned.
   Else return (60 - minutes) as string
   """
   mins = minutes if minutes < 30 else 60 - minutes
   #return mins if TEN_TO_TWENTY[mins] else f'{TEN_TO_TWENTY[20]}-{DECIMAL_BASE_DIGITS[minutes % 10]}'
   if DECIMAL_BASE_DIGITS.get(mins):
      return DECIMAL_BASE_DIGITS.get(mins)
   elif TEN_TO_TWENTY.get(mins):
      return TEN_TO_TWENTY.get(mins)
   else:
      return f'{TEN_TO_TWENTY[20]}-{DECIMAL_BASE_DIGITS[mins % 10]}'

def time_in_words(timestr):
   """
   Transform given time string argument into phrase.
   [!] --> expected time string format: 'HH:MM'
   """
   # add arg check with regex
   hours, minutes = map(int, timestr.split(':'))
   if minutes == 0:
     return f'{hours} o\'clock'
   elif minutes < 30:
      if minutes == 15:
         return f'quarter past {get_hours(hours)}'
      else:
         return f'{get_minutes(minutes)} past {get_hours(hours)}'
   elif minutes == 30:
      return f'half past {get_hours(hours)}'
   else:
      if minutes == 45:
         return f'quarter to {get_hours(hours)}'
      else:
         return f'{get_minutes(minutes)} to {get_hours(hours)}'
   

print(time_in_words('16:37'))