import math


def primefinder(limit):
    '''Returns a list containing the prime numbers up to and including the
    square root of the specified limit'''
    result = []
    for j in range(2, int(math.sqrt(limit)+1)):
        if is_prime(j):
            result.append(j)
    return result


def is_prime(num):
    '''Returns a Boolean of whether a number is prime or not'''
    for i in range(2, int(math.sqrt(num)+1)):
        if (num % i) == 0:
            return False
    return True


def largest_prime_factor(target):
    '''Prints the largest prime factor of the specified target'''
    prime_list = primefinder(target)
    biggest_factor = 0
    for k in prime_list:
        if target % k == 0:
            biggest_factor = k
    print biggest_factor


largest_prime_factor(600851475143)
