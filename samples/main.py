import sys
from pyo import *
from time import sleep


s= Server().boot()
s.start()
sf = SfPlayer("Run.aiff", speed=1, loop=True)
frq = 
#f = Tone(sf, frq).mix(2).out()


c = "unknown"
print "Please unlock Myo"
lock = True
while True:
    f = Tone(sf, frq).mix(2).out()
    fl = open("DATA.txt","r")
    g = fl.readline().strip()
    if not g: g=c
    if g!=c:
        print frq
        c = g
        if g =="waveIn":
            frq 
        elif g=="waveOut":
            frq += 200
            

    
    
    
    
    
        
    
