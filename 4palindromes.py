def is_palindrome(target):
    '''Returns a Boolean ofwhether a number is a palindrome or not'''
    return str(target) == str(target)[::-1]


def largest_palindrome_product(a, b):
    '''Prints the largest palindromic number with factors in the specified
    range, 'a' being the low end and 'b' being the high.'''
    biggest = 0
    for i in range(a, b):
        for j in range(a, b):
            target = i*j
            if is_palindrome(target):
                if target > biggest:
                    biggest = target
    print biggest

largest_palindrome_product(100, 999)
