total = 0
lastfib = 1
currentfib = 1
fibholder = 0
while currentfib < 4000000:
    print currentfib
    if currentfib % 2 == 0:
        total += currentfib
    fibholder = currentfib
    currentfib += lastfib
    lastfib = fibholder

print "The total is %s " % total
    
