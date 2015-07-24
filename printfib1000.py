lastfib = 1
currentfib = 1
fibholder = 0

while currentfib < 1000:
    print currentfib
    fibholder = currentfib
    currentfib += lastfib
    lastfib = fibholder
