#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 10:01:29 2020

@author: edgar
"""

import datetime 

today = datetime.datetime.today()
print("Today:", today)
oneday = datetime.timedelta(days = 1)
print("Yesterday:", today - oneday)
print("Tomorrow:", today + oneday)


print("\n\n---Day difference---")

date1 = datetime.datetime(2020,5,22,0,0,0,0)
date2 = datetime.datetime.today()
date3 = date1 - date2

print ("Difference in days:", date3.days)
print("Difference in seconds", date3.seconds)
print(type(date3))

