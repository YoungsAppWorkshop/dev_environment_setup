#!/usr/bin/env python3

import datetime
import pytz
from tzlocal import get_localzone


# Naive datetime: Easy to handle
# Aware datetime: Detail information (timezone, daylight savings times)


"""
    Example 1. Naive datetime
        - Basic usage of datetime.date
"""
d = datetime.date(2016, 7, 24)
tday = datetime.date.today()
print('Date:\t\t\t', d)
print('Today:\t\t\t', tday)
print('tday.year:\t\t', tday.year)
print('tday.month:\t\t', tday.month)
print('tday.day:\t\t', tday.day)

# weekday:      Monday 0     Sunday 6
print('tday.weekday():\t\t', tday.weekday())
# isoweekday:   Monday 1     Sunday 7
print('tday.isoweekday():\t', tday.isoweekday())


"""
    Example 2. Naive datetime
        - Working with timedelta
"""
# date2 = date1 +(-) timedelta
# timedelta = date1 +(-) date2

tdelta = datetime.timedelta(days=7)
print('tdelta = datetime.timedelta(days=7)')
print('tday + tdelta:\t\t', tday + tdelta)
print('tday - tdelta:\t\t', tday - tdelta)

tdelta = datetime.timedelta(hours=24)
print('tdelta = datetime.timedelta(hours=24)')
print('tday + tdelta:\t\t', tday + tdelta)
print('tday - tdelta:\t\t', tday - tdelta)

bday = datetime.date(2018, 4, 24)
till_bday = bday - tday
print('bday - tday:\t\t', till_bday)
print('till_bday.total_seconds():\t', till_bday.total_seconds())


"""
    Example 3. Naive datetime
        - Basic usage of datetime.time
"""
t = datetime.time(9, 30, 45, 100000)
print('datetime.time:\t\t', t)
print('t.hour:\t\t\t', t.hour)


"""
    Example 4. Naive datetime
        - Basic usage of datetime.datetime
"""
dt = datetime.datetime(2018, 4, 24, 9, 30, 45, 100000)
print('datetime.datetime:\t', dt)
print('dt.date():\t\t', dt.date())
print('dt.time():\t\t', dt.time())
print('dt.year:\t\t', dt.year)
print('dt.month:\t\t', dt.month)
print('dt.day:\t\t\t', dt.day)


"""
    Example 5. Naive datetime
        - Datetime constructors
"""
# today():  Current Local datetime with a timezone of none
dt_today = datetime.datetime.today()
# now():    You can pass a timezone paremeter
dt_now = datetime.datetime.now()
# utcnow(): Current UTC datetime with a timezone of none
dt_utcnow = datetime.datetime.utcnow()
print('dt_today:\t\t', dt_today)
print('dt_now:\t\t\t', dt_now)
print('dt_utcnow:\t\t', dt_utcnow)


"""
    Example 6. Aware datetime
        - Working with pytz library
        - Timezone Aware Datetime constructors
"""
# pytz is a third party library
#   - pip3 install pytz
dt = datetime.datetime(2018, 4, 24, 9, 30, 45, tzinfo=pytz.UTC)
dt_now = datetime.datetime.now(tz=pytz.UTC)
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print('Aware dt_today:\t\t', dt)
print('Aware dt_now:\t\t', dt_now)
print('Aware dt_utcnow:\t', dt_utcnow)

# Changing Timezone
dt_mtn = dt_now.astimezone(pytz.timezone('US/Mountain'))
print('US/Mountain:\t\t', dt_mtn)

# To view all timezones in pytz library,
# for tz in pytz.all_timezones:
#     print(tz)


"""
    Example 7. Aware datetime
        - Getting pytz compatible Local Timezone
        - Converting Naive datetime to Aware datetime
"""
# To get pytz compatible Local Timezone,
#   - pip3 install tzlocal
#   - get_localzone()

# Current Timezone
tz = get_localzone()
print('Current Timezone:\t', tz)

# Converting Naive datetime to Aware datetime
dt_naive = datetime.datetime.now()
dt_aware = tz.localize(dt_naive)
print('dt_naive:\t\t', dt_naive)
print('dt_aware:\t\t', dt_aware)


"""
    Example 7. Formatting Datetime
        - Converting datetime to String
        - Converting String to datetime
"""
dt_str = 'July 26, 2016'
print('dt_naive.isoformat():\t', dt_naive.isoformat())
print('dt_aware.isoformat():\t', dt_aware.isoformat())
# Converting datetime to String
print('strftime("%B %d, %Y"):\t', dt_aware.strftime('%B %d, %Y'))
# Converting String to datetime
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print('strptime("%B %d, %Y"):\t',  dt)
