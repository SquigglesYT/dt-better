# dt-better
a pretty lightweight datetime wrapper.

to install this, run pip install dt-better in your terminal.
pip comes with most modern python versions.

examples:

```python
import dt_better as dt
date = dt.current_date()
print(date)
```

```python
import dt_better as dt
tomorows_date = dt.tomorrow()
print("Tomorrows Date is:", tomorrows_date)
```


current_date(): this returns the current date

current_time(): this returns the current time

current_time_without_seconds(): this returns the current time without seconds

current_month(): this returns the current month as a string

current_month_number(): this returns the current month but as a number

current_day_of_month(): this shows what day of the month you are on as a number

current_year(): this returns the current year

current_day_of_week(): this returns the current day of the week, sunday monday tuesday wednesday thursday friday or saturday

current_hour(): this returns the current hour

current_minute(): this returns the current minute

current_second(): this returns the current second

yesterday(): this returns yesterdays date

tomorrow(): this returns tomorrows date
