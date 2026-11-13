import math


#PSEUDOCODE

input bps
input btg

timeleft = btg/bps

timeleft = round timeleft down to the nearest second

if timeleft == 1:
    sec = 'second'
else
    sec = 'seconds'
    
print "The download will take approximately {timeleft} {sec}"
