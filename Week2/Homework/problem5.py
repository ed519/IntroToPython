import datetime
#import time
import calendar

b_day = datetime.date(1999,4,12)
print(b_day)
print("B day year:", b_day.year)
print("B month:", b_day.month)
print("B day:", b_day.day)
print("Week:" , b_day.weekday())

d_now = datetime.date.today()
next_b_day = datetime.date(2020,4,12)
print("Next b day:", next_b_day - d_now)
print("\n")
c = calendar.TextCalendar(calendar.SUNDAY)
calend = c.formatmonth(2017,5)
print(calend)

date_delta = datetime.timedelta(days = 1)
yesterday = d_now - date_delta
print("Yesterday:", yesterday)


date_delta = datetime.timedelta(days = 2)
print("Yesterday + 2 days:", yesterday + date_delta)


date_delta = datetime.timedelta(days = 3)
print("Yesterday - 3:", yesterday - date_delta)