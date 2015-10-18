""" Given two dates, calculate days between the dates """
"""This is my solution to the Udacity Intro to Computer Science class lesson 2 problem set(optonal 2) problem 2(Days Old)"""
#my code below
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    md1=md(month1,year1)
    md2=md(month2,year2)
    yd1=yd(year1)
    yd2=yd(year2)
    mresult1=0
    mresult2=0
    yresult=0
    for i in range(1,month1):
        mresult1=mresult1+md(i,year1)
    for i in range(1,month2):
        mresult2=mresult2+md(i,year2)
    for i in range(year1,year2):
        yresult=yresult+yd(i)
    return yresult+mresult2-mresult1+day2-day1
def yd(y):
    if y%4==0:
        if y%100==0:
            if y%400!=0:
                return 365
        return 366
    return 365
        
def md(month1,y):
    if month1==1 or month1==3 or month1==5 or month1==7 or month1==8 or month1==10 or month1==12:
        md=31
    elif month1==2:
        if yd(y)==365:
            md=28
        else:
            md=29
    else:
        md=30
    return md

# Udacity test code
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