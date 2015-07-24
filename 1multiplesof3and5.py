def main(a, b, limit):
    """Finds the sum of all multiples of 'a' or 'b' below 'limit'"""
    answer = 0
    for i in range(1, limit):
        if i % a == 0 or i % b == 0:
            answer += i
    print "The sum of all multiples of %s and %s is %s." % (a, b, answer)


main(3, 5, 1000)
