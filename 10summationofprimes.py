import math


def is_prime(num):
    '''Returns a Boolean of whether a number is prime or not'''
    for i in range(2, int(math.sqrt(num)+1)):
        if (num % i) == 0:
            return False
    return True


def main_search(limit):
    summation = 0
    for i in range(2, limit):
        if is_prime(i):
            summation += i
    print "The summation of all primes below %s is %s." % (limit, summation)


main_search(2000000)
