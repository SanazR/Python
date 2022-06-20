import calendar

#print(calendar.weekheader(3))
#print()

#print(calendar.firstweekday())
#print()

#print(calendar.month(2021,4,3))

#print hte month like a matrix
#print(calendar.monthcalendar(2021,4))

#print(calendar.calendar(2022))

Day_of_the_week= calendar.weekday(2025,3,8)
print(Day_of_the_week)

is_leap= calendar.isleap(2020)
print(is_leap)

how_many_leap_days= calendar.leapdays(2000,2004) 
#This funct is exclusive bc 2004 is a leap year and if it was inclusive we would have got 2 as a result.

print(how_many_leap_days)

