import sys

c = "unknown"
print "Please unlock Myo"
lock = True
while True:
    f = open("DATA.txt","r")
    g = f.readline().strip(' \n')
    if lock and g!="unknown":
        print "Myo Unlocked!"
        print g
        c = g
        lock = False
    if not lock and g=="unknown":
        print "Myo Locked"
        lock = True

    if not lock and c!=g:
        print g
        c = g
        

    
    
    
    
    
    
        
    
