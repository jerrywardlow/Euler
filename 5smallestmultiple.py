def check_multiple(target, a, b):
    '''Returns whether a number 'target' is evenly divisible by all numbers
    'a' through 'b' inclusive.'''
    for i in range(a, b+1):
        if target % i != 0:
            return False
    return True


def list_sum(a, b):
    product = 1
    target_list = range(a, b+1)
    for x in target_list:
        product *= x
    return product


def smallest_multiple(a, b):
    for x in range(1, list_sum(a, b)):
        if check_multiple(x, a, b):
            print x
            break


def small_mult(a, b):
    x = 1
    while check_multiple(x, a, b) != True:
        x += 1
    print x

small_mult(1, 20)
