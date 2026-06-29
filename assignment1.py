#!/usr/bin/env python3

'''
OPS445 Assignment 1
Program: assignment1.py 
Author: "Student Name"
Semester: "Fall/Winter/Summer YYYY"

The python code in this file (assignment1.py) is original work written by
"Student Name". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

import sys

def day_of_week(year: int, month: int, date: int) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7
    return days[num]


def leap_year(year: int) -> bool:
    """
    Returns True if the year is a leap year.
    Returns False otherwise.
    """

    if year % 400 == 0:
       return True

    if year % 100 == 0:
       return False

    if year % 4 == 0:
       return True

    return False


def mon_max(month: int, year: int) -> int:
    """
    Returns the maximum day for a given month.
    Includes leap year check.
    """

    if month == 2:
        if leap_year(year):
            return 29
        return 28

    month_days = {
        1: 31,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    return month_days[month]


def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function takes care of the number of days in February for leap year.
    This fucntion has been tested to work for year after 1582
    '''
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)

    month_max = mon_max(month, year)

    tmp_day = day + 1  # next day

    if tmp_day > month_max:
        to_day = tmp_day % month_max  # if tmp_day > this month's max, reset to 1 
        tmp_month = month + 1
    else:
        to_day = tmp_day
        tmp_month = month + 0

    if tmp_month > 12:
        to_month = 1
        year = year + 1
    else:
        to_month = tmp_month + 0

    next_date = f"{year}-{to_month:02}-{to_day:02}"

    return next_date


def usage():
    "Print a usage message to the user"
    
    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD")
    sys.exit()

def valid_date(date: str) -> bool:
    try:
        str_year, str_month, str_day = date.split('-')

        if len(str_year) != 4:

            return False



        year = int(str_year)

        month = int(str_month)

        day = int(str_day)



        if month < 1 or month > 12:

             return False



        if day < 1:

             return False



        if day > mon_max(month, year):

            return False

        return True

    except:

        return False

def day_count(start_date: str, stop_date: str) -> int:
    "Loops through range of dates, and returns number of weekend days"
    count = 0



    current_date = start_date



    while current_date <= stop_date:



        year, month, day = current_date.split('-')



        weekday = day_of_week(

            int(year),

            int(month),

            int(day)

        )


        if weekday == 'sat' or weekday == 'sun':

            count += 1


        current_date = after(current_date)




    return count

if __name__ == "__main__":

    # Check that exactly two dates were entered
    if len(sys.argv) != 3:
        usage()

    # Get the dates from the command line
    date1 = sys.argv[1]
    date2 = sys.argv[2]

    # Make sure both dates are valid
    if not valid_date(date1):
        usage()

    if not valid_date(date2):
        usage()

    # Put the earlier date first
    if date1 <= date2:
        start_date = date1
        stop_date = date2
    else:
        start_date = date2
        stop_date = date1

    # Calculate the number of weekend days
    weekend_days = day_count(start_date, stop_date)

    # Display the result
    print(f"The period between {start_date} and {stop_date} includes {weekend_days} weekend days.")
