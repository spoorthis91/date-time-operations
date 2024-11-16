import datetime

#  Get current date and time
current_datetime = datetime.datetime.now()
print("Current Date and Time:", current_datetime)

#  Get the current date
current_date = datetime.date.today()
print("Current Date:", current_date)

# Get the current time
current_time = datetime.datetime.now().time()
print("Current Time:", current_time)

# Creating a specific date (year, month, day)
specific_date = datetime.date(2024, 11, 17)
print("Specific Date:", specific_date)

# Creating a specific time (hour, minute, second)
specific_time = datetime.time(14, 30, 45)
print("Specific Time:", specific_time)

# Adding days to a date (e.g., add 10 days to the current date)
days_to_add = datetime.timedelta(days=10)
new_date = current_date + days_to_add
print("Date after 10 days:", new_date)

# Subtracting days from a date (e.g., subtract 5 days from the current date)
days_to_subtract = datetime.timedelta(days=-5)
new_date_subtract = current_date + days_to_subtract
print("Date 5 days ago:", new_date_subtract)

# Formatting dates and times (using strftime)
formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date and Time:", formatted_date)

# Parsing a string into a date (using strptime)
date_string = "2024-11-17 14:30:45"
parsed_datetime = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Parsed Date and Time:", parsed_datetime)

# Get the difference between two dates (e.g., days between two dates)
date1 = datetime.date(2023, 5, 10)
date2 = datetime.date(2024, 11, 17)
difference = date2 - date1
print("Days between two dates:", difference.days)

# Get the weekday name for the current date (e.g., Monday)
weekday_name = current_date.strftime("%A")
print("Weekday Name:", weekday_name)

# Get the day of the year
day_of_year = current_date.timetuple().tm_yday
print("Day of the Year:", day_of_year)
