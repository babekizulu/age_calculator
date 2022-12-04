import datetime
# PROGRAM STARTS
# get user's date of birth
print('Please enter your date of birth')
year_raw = input('yyyy: ')
month_raw = input('mm: ')
day_raw = input('dd: ')
year = int(year_raw)
# PARSE INPUTS TO INTEGER
# check if month which user provided is single or double digit
if (month_raw[0] == '0'):
    month = int(month_raw[1])
else:
    month = int(month_raw)
# check if day which user provided is single or double digit
if (day_raw[0] == '0'):
    day = int(day_raw[1])
else:
    day = int(day_raw)
# PARSE CURRENT DATE TO INTEGER
# define current year, month & day
current_date = datetime.date.today().__str__()
current_year = int(current_date[0:4])
# check if current month is single or double digit
if (current_date[5:7][0] == '0'):
    current_month = int(current_date[6])
else:
    current_month = int(current_date[5:7])
# check if current day is single or double digit
if (current_date[-2:][0] == '0'):
    current_day = int(current_date[-1])
else:
    current_day = int(current_date[-2:])
# TEST PARSED DATES
# # test value of current year, month & day
# print(current_year, current_month, current_day) [TEST PASSED!]
# # test value of year, month & day which user provided
# print(year, month, day) [TEST PASSED!]

# DETERMINE YEARS, MONTHS & DAYS ELAPSED
# determine whether current month is less than or greater than
# the month which the user provided
if (current_month < month):
    past_birth_month = False
else:
    past_birth_month = True
# if the current month is before the user's birth month
# set age_years to age_years - 1 since they have not aged up yet
if (past_birth_month == False):
    age_years = (current_year - year) - 1
else:
    age_years = current_year - year
# if the current month is before the user's birth month
# calculate months until user's birth month
# then subtract this value from 12 to determine months elapsed since
# users last birth month and store as age_months
if (past_birth_month == False):
    months_until = month - current_month
    months_elapsed = 12 - months_until
    age_months = months_elapsed
# if the current month is after the user's birth month
# calculate months elapsed since user's birth month and store as age_months
else:
    months_since = current_month - month
    age_months = months_since
# print user's age in years and months
print(f"You are {age_years} years & {age_months} months old")
