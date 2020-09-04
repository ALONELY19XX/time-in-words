from .timestrings import *

def get_hours(hours):
   """
   Get AM/PM hours --> 1 => 1, 2 => 2, ..., 13 => 1, 14 => 2, ...
   """
   #return 12 if (hours == 12 or hours == 0) else hours % 12
   h = 12 if (hours == 12 or hours == 0) else hours % 12
   if DECIMAL_BASE_DIGITS.get(h):
      return DECIMAL_BASE_DIGITS.get(h)
   else:
      return TEN_TO_TWENTY[h]
   

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

def append_minutes(minutes, should_append):
   if minutes == 1 and should_append:
      return ' minute'
   return ' minutes' if should_append else ''