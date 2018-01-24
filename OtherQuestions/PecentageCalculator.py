def calculate(base, percentage=1, days=365):

    for day in xrange(days):
        p = base * percentage/100.0
        base+=p
        pass
    return base



print 'With $1500 Investment, In 3 Months : ' , calculate(1500,percentage=3,days=90)
print 'With $1500 Investment, In 6 Months : ' , calculate(1500,percentage=3,days=180)
print 'With $1500 Investment, In 1 Year   : ' , calculate(1500,percentage=3,days=365)



