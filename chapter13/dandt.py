import datetime
x=datetime.datetime.now()# 1st dt is module 2nd dt is object
print(x)# gives current time

x=datetime.datetime(2021,1,18)#yy-mm-dd
print(x)

now=datetime.datetime.now()
#year=now.strftime("%y")#last to digits
#year=now.strftime("%Y")#full year
year=now.strftime("%b")
year=now.strftime("%B")
year=now.strftime("%m")
year=now.strftime("%H")
year=now.strftime("%I")
year=now.strftime("%p")
year=now.strftime("%M")
print(year)

from datetime import datetime, timedelta

today = datetime.now()
future = today + timedelta(days=5)

print(future)

from datetime import date

today = date.today()
print(today)