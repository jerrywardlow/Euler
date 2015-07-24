def run_collatz(num):
    """Finds the number of terms in the Collatz chain of 'num'"""
    count = 1
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = num*3 + 1
        count += 1
    return count
    #print "The chain contains %s terms." % count


def main(limit):
    """Finds the longest Collatz chain with starting integer < 'limit'"""
    number = 0
    longest_chain = 0
    for i in range(1, limit):
        working_chain = run_collatz(i)
        if working_chain > longest_chain:
            number = i
            longest_chain = working_chain
    print "The longest chain is %s terms produced by %s." % (longest_chain,
                                                             number)


main(1000000)
