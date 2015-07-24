def power_digit_sum(num, power):
    """Returns the sum of individual digits within 'num**power'"""
    total = 0
    for i in str(num**power):
        total += int(i)
    print "The total is %s." % total


power_digit_sum(2, 1000)
