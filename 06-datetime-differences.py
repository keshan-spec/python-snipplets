import datetime


today = datetime.datetime.today()
print(today)

date_from = datetime.date(2019, 10, 8)
date_to = datetime.date(2019, 11, 6)

diff = date_to-date_from
print(diff)

days = diff.days
print(days)
