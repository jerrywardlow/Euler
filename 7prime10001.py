import math

def is_prime(num):
    '''Returns a Boolean of whether a number is prime or not'''
    for i in range(2, int(math.sqrt(num)+1)):
        if (num % i) == 0:
            return False
    return True

def prime_time(n):
    '''Spits out the nth prime number'''
    counter = 0
    work = 1
    while counter != n:
        work += 1
        if is_prime(work):
            counter += 1
    print "The prime number at position %s is %s" % (n, work)

prime_time(10001)
