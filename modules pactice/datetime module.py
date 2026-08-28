import datetime

birthday = datetime.date(2026, 7, 10)
print(birthday)

tday = datetime.date.today()
print(tday)

duration = tday - birthday      # timedelta created
print(duration)
print(duration.days)
print(duration.seconds)
print(duration.microseconds)
print(duration.total_seconds())

confusion = datetime.datetime(2009,2,5)
print(confusion)