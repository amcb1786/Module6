#Question 1
# Revised code
import sys
for line in sys.stdin:
 data = line.strip().split("\t")
if len(data) == 6:
    date, time, store, item, cost, payment = data
print("{0}\t{1}".format(item, cost))
# Corrected the print method by adding parentheses was utilizing outdated print function.
# Python is still unable to generate an output because "data, item, and cost" are undefined.
# Question 2
datetime import datetime
from datetime import timedelta

# add 1 day
print(datetime.now() + timedelta(days=1))
# subtract 60 seconds
print(datetime.now() - timedelta(seconds=60))
# add 2 years
# timedelta only can be calculated in days, seconds, and microseconds
# converting 2 years to days = 730 days
print(datetime.now() + timedelta(days=730))
# Question 3
datetime import datetime
from datetime import timedelta
d = timedelta(microseconds=-1)
print(d.days, d.seconds, d.microseconds)
# create a timedelta object representing 100 days, 10 hours, and 13 minutes.
# since timedelta can only be displayed in days, seconds, and microseconds
# convert 100 days, 10 hours, and 13 minutes to 144613 minutes
e = timedelta(minutes=144613)
print(e.days, e.seconds, e.microseconds)

# Question 4
from datetime import datetime

datetime_object: datetime = datetime.now()

# create a class to output two arguments
class DateTime:

    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches
        self.time = datetime_object

    def function(self):
        print(f"My height is equal to:{self.feet} feet, and {self.inches} inches, the time is:{self.time}")
# format string
# use curly brackets to output desired height and time

enter_height = DateTime(5, 2)
print(enter_height.function())
