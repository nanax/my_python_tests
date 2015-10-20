"""Given two dates, calculate days between the dates.Assumes inputs are valid dates in Gregorian calendar. """
"""This is another solution to the Udacity Intro to Computer Science class lesson 2 problem set(optonal 2) problem 2(Days Old),included in lesson 2.5"""
def is_leap(year, month, day):
    if year%4==0:
        a=True
        if year%100==0:
            if year%400!=0:
                a=False
    else:
        a=False
    if a:
        if month==2:
            if day==29:
                return True
    return False
def nextDay(year, month, day):
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        if day < 31:
            return year, month, day + 1
        else:
            if month == 12:
                return year + 1, 1, 1
            else:
                return year, month + 1, 1
    elif month==2:
        if is_leap(year, month, day+1):           #tricky,pay attention
            return year, month, day + 1
        else:
            if day < 28:
                return year, month, day + 1
            else:
                return year, month + 1, 1
    else:
        if day < 30:
            return year, month, day + 1
        else:
            return year, month + 1, 1   
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False        

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days
#Udacity test code
def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()

#for convenience
i=raw_input("press any key to continue")