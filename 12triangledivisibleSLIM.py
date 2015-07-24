def factor_count(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count

def main(limit):
    count = 1
    triangle = 1
    while True:
        factors = factor_count(triangle)
        if factors > limit:
            print "Our magic triangle is %s with %s factors." % (triangle,
                                                                 factors )
            break
        count += 1
        triangle += count

main(5)
