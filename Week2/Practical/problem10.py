import datetime
#import time 
#import caldendar

dt_now = datetime.datetime.now()


print(dt_now)
print("Year:", dt_now.year)
print("Month:", dt_now.month)
print("Week:", dt_now.weekday())

tdelta = datetime.timedelta(days= 5)

print("-5 days:", dt_now - tdelta)
tdelta = datetime.timedelta(seconds= 5)
print("+5 seconds:", dt_now + tdelta)
