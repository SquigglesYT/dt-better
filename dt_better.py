from datetime import date, datetime, timedelta

def now():
    return datetime.now()

def current_date():
    return date.today()

def current_time():
    return now().time()

def current_time_without_seconds():
    return now().strftime("%H:%M")

def current_month():
    return now().strftime("%B")

def current_month_number():
    return now().month

def current_day_of_month():
    return now().day

def current_year():
    return now().year

def current_day_of_week():
    return now().strftime("%A")

def current_hour():
    return now().hour

def current_minute():
    return now().minute

def current_second():
    return now().second

def yesterday():
    return date.today() - timedelta(days=1)

def tomorrow():
    return date.today() + timedelta(days=1)