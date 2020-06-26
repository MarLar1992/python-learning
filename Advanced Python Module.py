import datetime
mytime = datetime.time(13,20,1,20)
mytime.minute

mytime.hour
print(mytime.minute)
print(mytime.hour)
print(mytime)
print(mytime.microsecond)

from datetime import date
date1 = date(2021,11,3)
date2 = date(2020,11,3)

result = date1 - date2
print (result)
result.days

datetime1 = datetime (2021,11,3,22,0)
datetime2 = datetime (2021,11,3,12,0)
mydiff = datetime1 - datetime2
print (mydiff.seconds)

print (mydiff.total_seconds())