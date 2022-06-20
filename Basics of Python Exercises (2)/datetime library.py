import datetime
import pytz

#Thislibrary considered all the leap years, different days in a months and ect. It is basically time saving and easier to use.

#datetime.time(h, min, sec, ms)
#datetime.date(y, m, d)
#datetime.datetime(y, m, d, h, min, sec, ms)

#Monday=0, Tuesday=1

today=datetime.date.today()
print(today)

birthday= datetime.date(1994,4,5)
print(birthday)
print()

days_since_birth=today-birthday
days_since_birth1=(today-birthday).days

print(days_since_birth)
print(days_since_birth1)
print()

#Add 10 days to current day
tdelta=datetime.timedelta(days=10)
print(today + tdelta)
print(today - tdelta)
print()

print(today.month)
print(today.day)
print(today.weekday())
print()

print(datetime.time(7,2,22,15))
print()

#Add 10 h to current day
hour_delta=datetime.timedelta(hours=10)
print(datetime.datetime.now()+hour_delta)
print()

#Timezone
datetime_today= datetime.datetime.now(tz=pytz.UTC)
datetime_pacific= datetime_today.astimezone(pytz.timezone('US/pacific'))
print(datetime_pacific)

#print all the timezones
#for tz in pytz.all_timezones:
#  print(tz)



#Stringformatting with dates
#2021-10-12 --> 12th of Oct 2021
#We should use strftime which f= formatting

print(datetime_pacific.strftime('%B %d, %Y'))
print()

#October 12, 2021 --> 2021-10-12
#We should use strptime which p=parsing
datetime_reverse=datetime.datetime.strptime('October 12, 2021', '%B %d, %Y')

print(datetime_reverse)
print(repr(datetime_reverse))






