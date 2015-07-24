triangle = 1
count = 1
length = 1
while True:
    wapple = []
    for i in range(1, triangle + 1):
        if triangle % i == 0:
            wapple.append(i)
    length = len(wapple)
    print "%s has %s factors." % (triangle, length)
    if length > 500:
        print "Our magic triangle is %s" % (triangle)
        break
    count += 1
    print "Next number to add is %s" % (count)
    triangle += count
    print "Next Triangle is %s" % (triangle)

