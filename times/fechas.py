import datetime

time_now = datetime.datetime.now()
print(time_now)

time_now = datetime.date.today()
print(time_now)

print(time_now.year)
print(time_now.month)
print(time_now.day)

print()

#Codigos de formato
# %Y Year
# %m month
# %d day
# %H hour
# %M minute
# %S second

my_datetime = datetime.datetime.now()

print(f"LATAM: {my_datetime.strftime('%d/%m/%Y')}")
print(f"USA: {my_datetime.strftime('%m/%d/%Y')}")
print(f"YEAR {my_datetime.strftime('%Y')}")