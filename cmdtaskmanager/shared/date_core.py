import datetime
import pytz


DATE_FORMAT = '%Y-%m-%d'
DATETIME_FORMAT = f'{DATE_FORMAT} %H:%M:%S'

def format_to_local_d(utc_dt):
    local_dt = utc_to_local_tz(utc_dt)
    return format_d(local_dt)

def format_to_local_dt(utc_dt):
    local_dt = utc_to_local_tz(utc_dt)
    return format_dt(local_dt)

def get_local_tz():
    now = datetime.datetime.now()
    local_now = now.astimezone()
    local_tz = local_now.tzinfo
    local_tzname = local_tz.tzname(local_now)
    return local_tzname

def format_dt(dt):
    return dt.strftime(DATETIME_FORMAT)

def format_d(d):
    return d.strftime(DATE_FORMAT)

def utc_to_local_tz(dt):
    local_timezone = pytz.timezone(get_local_tz())
    local_datetime = dt.replace(tzinfo=pytz.utc)
    return local_datetime.astimezone(local_timezone)

