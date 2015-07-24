def sum_square(x):
    '''1 squared plus 2 squared plus 3 squared...'''
    total = 0
    for i in range(1, x+1):
        total += i**2
    return total


def square_sum(x):
    '''(1+2+3+4+5...) squared'''
    return sum(range(1, x+1))**2


def print_result(num):
    print "The range is 1 through %s" % num
    print "The sum of the squares is: %s" % sum_square(num)
    print "The square of the sum is: %s" % square_sum(num)
    print ("The difference between the sum of the squares and the square of "
           "the sum is: %s" % (square_sum(num) - sum_square(num)))

print_result(100)
