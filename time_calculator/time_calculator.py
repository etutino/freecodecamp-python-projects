def add_time(start, duration, day=False):
  # Days of the week list
  days_of_the_week = [
    'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday',
    'saturday'
  ]

  # Converting the day specified to lowercase to match the days in the days_of_the_week list
  if day:
    day = day.lower()

  # Splitting the duration and converting to integers
  duration_hour_string, duration_minute_string = duration.split(":")
  duration_hours = int(duration_hour_string)
  duration_minutes = int(duration_minute_string)

  # Grabbing the hours, minutes and AM/PM from the start time
  start_hour_string, start_minute_string_ampm = start.split(":")
  start_hours = int(start_hour_string)
  start_minute_string, start_pm_am = start_minute_string_ampm.split(" ")
  start_minutes = int(start_minute_string)

  # Converting the start hours to military time
  if start_pm_am == 'AM' and start_hours == 12:  # Special case: 12:00 AM should be 00:00 in military time
    start_hours = 0
  elif start_pm_am == 'PM' and start_hours == 12:  # Special case: 12:00 PM should remain 12:00 in military time
    start_hours = 12
  elif start_pm_am == 'PM' and start_hours < 12:
    start_hours += 12
  else:
    start_hours = start_hours

  # Calculating total minutes of the starting time
  total_start_minutes = start_hours * 60 + start_minutes

  # Calculating total minutes of the duration
  total_duration_minutes = duration_hours * 60 + duration_minutes

  # Calculating total minutes of the new time
  total_new_minutes = total_start_minutes + total_duration_minutes

  # Converting the total new minutes to hours. Calculating the remainder as the minutes
  new_hours = int(total_new_minutes // 60)
  new_minutes = int(total_new_minutes % 60)

  hour_within_24_hours = new_hours % 24

  if hour_within_24_hours == 0:
    new_hours_12 = 12
    new_pm_am = 'AM'
  elif 1 <= hour_within_24_hours <= 11:
    new_hours_12 = hour_within_24_hours
    new_pm_am = 'AM'
  elif hour_within_24_hours == 12:
    new_hours_12 = 12
    new_pm_am = 'PM'
  else:
    new_hours_12 = hour_within_24_hours - 12
    new_pm_am = 'PM'

  # If the minutes is only one digit, need to add a 0 in front
  if 0 <= new_minutes < 10:
    new_minutes = "0" + str(new_minutes)

  # Calculating number of days if the new time goes into the next day or more than 1 day later
  next_day = False
  days_later = 0
  if total_new_minutes >= (24 * 60):
    next_day = True
    days_later = total_new_minutes // (24 * 60)

  # If going into the next day or more than 1 day later, getting the new day of the week
  if day is not False:
    index_day = days_of_the_week.index(day)
    new_index_day = (index_day + days_later) % 7
    new_day = days_of_the_week[new_index_day]
    new_day = new_day.capitalize()

  # String that puts together the new hours and minutes for the new time
  new_time = str(new_hours_12) + ":" + str(new_minutes) + " " + new_pm_am

  # Printing the new time and how many days later the new time is
  if day is not False:
    if days_later == 1:
      print(new_time + " (next day)")
    elif days_later == 0:
      print(new_time + ", " + new_day)
    else:
      print(new_time + ", " + new_day + " (" + str(days_later) +
            " days later)")
  elif day is False:
    if days_later == 1:
      print(new_time + " (next day)")
    elif days_later == 0:
      print(new_time)
    else:
      print(new_time + " (" + str(days_later) + " days later)")
  else:
    print(new_time)
