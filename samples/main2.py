import sys
from pyo import *
from time import sleep


s= Server().boot()
s.start()
sf = SfPlayer("M.aiff", speed=1, loop=True)
frq = 1000
#f = Tone(sf, frq).mix(2).out()

b1 = Allpass(sf, delay=[.0204,.02011], feedback=0.25)
b2 = Allpass(b1, delay=[.06653,.06641], feedback=0.31)
b3 = Allpass(b2, delay=[.035007,.03504], feedback=0.4)
b4 = Allpass(b3, delay=[.023021 ,.022987], feedback=0.55)
c1 = Tone(b1, 5000, mul=0.2)
c2 = Tone(b2, 3000, mul=0.2)
c3 = Tone(b3, 1500, mul=0.2)
c4 = Tone(b4, 500, mul=0.2)

revI = 0

dls = [[.0204,.02011],[.06653,.06641],[.035007,.03504],[.023021 ,.022987]]
fbs = [0.25,0.31,0.4,0.55]
cfrq = [5000,3000,1500,500]

c = "unknown"
print "Please unlock Myo"
lock = True
while True:
    sfT = Tone(sf, frq)
    bs = []
    for i in xrange(revI):
        bs.append(Allpass(sfT, delay=dls[i],feedback=fbs[i]))
    if revI==0:
        sfT.out()
        c1.stop(); c2.stop(); c3.stop(); c4.stop()
    if revI>=1:
        c1 = Tone(bs[0], cfrq[0], mul=0.2).out()
        c2.stop(); c3.stop(); c4.stop()
    if revI>=2:
        c2 = Tone(bs[1], cfrq[1], mul=0.2).out()
        c3.stop(); c4.stop()
    if revI>=3:
        c3 = Tone(bs[2], cfrq[2], mul=0.2).out()
        c4.stop()
    if revI>=4:
        c4 = Tone(bs[3], cfrq[3], mul=0.2).out()
            
    revI = input()
    fl = open("DATA.txt","r")
    line = fl.readline()
    #print line.split()
    
    if line:
        fr,gst = line.split()
        fr = int(fr)
        if fr:
            frq = int(fr)*125
        if not gst: gst = c
        if gst!=c:
            c = gst
            if gst == "waveIn":
                print "wavein"
                revI = max(0,revI-1)
            elif gst == "waveOut":
                print "waveout"
                s.pause()
                #revI = min(4,revI+1)
            
            

    
    
    
    
    
        
    
