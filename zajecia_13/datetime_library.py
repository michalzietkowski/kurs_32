import datetime
print(datetime.datetime.now())
print(type(datetime.datetime.now()))

subsctription_time = 31
print(f"Twoja subskrypcja właśnie się rozpoczeła {datetime.datetime.now()}, skończy się za 30 dni")

next_subscription_date = datetime.datetime.now() + datetime.timedelta(weeks=subsctription_time)
print(next_subscription_date)

todays_date = "2024-11-06"
todays_date_in_us_format = "2024/06/11 12:00:12"

format = "%Y/%d/%m %H:%M:%S"

todays_date_in_date_format = datetime.datetime.fromisoformat(todays_date)
print(todays_date_in_date_format)
print(type(todays_date_in_date_format))
print(datetime.datetime.strptime(todays_date_in_us_format, format))
print(type(datetime.datetime.strptime(todays_date_in_us_format, format)))
print(todays_date_in_date_format.year)
print(todays_date_in_date_format.month)
print(todays_date_in_date_format.day)