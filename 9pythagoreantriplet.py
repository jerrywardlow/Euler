def check_less(a, b, c):
    """Check to verify that a < b < c"""
    return (a < b < c)


def check_pyth(a, b, c):
    """Check to see if a squared plus b squared equals c squared"""
    return (a**2 + b**2 == c**2)


def check_total(a, b, c, total):
    """Check to see that a + b + c == 1000"""
    return (a + b + c == total)


def check_all(a, b, c, total):
    """Runs all three checks and returns a boolean of the combined result"""
    return (check_less(a, b, c) and
            check_pyth(a, b, c) and
            check_total(a, b, c, total))


def special_triplet(total):
    """Runs the search for a special Pythagorean triplet"""
    for c in range(3, total):
        for b in range(2, total):
            for a in range(1, total):
                if check_all(a, b, c, total):
                    print "The correct numbers are %s, %s and %s" % (a, b, c)


special_triplet(1000)
