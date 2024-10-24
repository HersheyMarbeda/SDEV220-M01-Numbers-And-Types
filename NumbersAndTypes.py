# Programmer: Hershey Marbeda
# Instructor: Mr. Hamby
# Course: SDEV 220: Soft. Dev. Using Python
# College: Ivy Tech Community College
# Program (last updated): 10.24.2024

# Variables
seconds = 60
minutes =  60
day = 24

# 3.2 Assign the result from the previous task (seconds in an hour) to a variable called seconds_per_hour.
seconds_per_hour = seconds * minutes
print(seconds_per_hour, "seconds per hour")

# 3.3 How many seconds are in a day? Use your seconds_per_hour variable.

seconds_per_day = seconds_per_hour * day
print(seconds_per_day, "seconds per day")

# 3.4 Calculate seconds per day again, but this time save the result in a variable called seconds_per_day.
seconds_per_day = seconds_per_hour * day
print(seconds_per_day, "seconds per day")

# 3.5 Divide seconds_per_day by seconds_per_hour. Use floating-point (/) division.
print(seconds_per_day / seconds_per_hour)

# 3.6 Divide seconds_per_day by seconds_per_hour, using integer (//) division. 
print(seconds_per_day // seconds_per_hour)

# Did this number agree with the floating-point value from the previous question, aside from the final .0?
# yes. In the world of Mathematics, it is logically accepted 24 or 24.0 since if we round it off to the nearest
# whole number it would just be 24