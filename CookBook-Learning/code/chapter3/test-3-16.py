from datetime import datetime, timedelta
from pytz import timezone, utc

d = datetime(2013, 3, 10, 1, 45)
print(d)
central = timezone('US/Eastern')
loc_d = central.localize(d)
print(loc_d)

band_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print(band_d)

later = loc_d + timedelta(minutes=30)
print(later)

later = central.normalize(loc_d + timedelta(minutes=30))
print(later)

utc_d = loc_d.astimezone(utc)
print(utc_d)

print(utc_d + timedelta(minutes=30))
print(utc_d.astimezone(central))