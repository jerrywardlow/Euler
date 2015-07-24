import math

def primefinder(limit):
    '''Returns a list containing the prime numbers up to and including the
    specified limit'''
    result = []
    for j in range(2, limit):
        if is_prime(j):
            result.append(j)
    return result

def is_prime(num):
    '''Returns whether a number is prime or not'''
    for i in range(2, int(math.sqrt(num)+1)):
        if (num % i) == 0:
            return False
    return True
