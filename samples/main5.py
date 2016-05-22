from pyo import *
import sys
from time import sleep

s = Server().boot()
s.start()

sf = SfPlayer("M.aiff", speed=1, loop=True)

a = FourBand(sf, freq1=500, freq2=800, freq3=1200, mul=.8)
mm = Mixer(outs=4, chnls=4, time = 0.025)
mm.addInput(0,a[1]);mm.addInput(1,a[2]);mm.addInput(2,a[3]);mm.addInput(3,a[4])
mm.setAmp(0,0,0.5);mm.setAmp(1,0,0.5);mm.setAmp(2,0,0.5);mm.setAmp(3,0,0.5);
chnl = 0
spec = Spectrum(mm[1],size=1024)
spec.polltime(1)
spec.poll(True) 
c = ""
pause = False
while True:
    mm.out()
    #fl = open("DATA.txt","r")
    #line = fl.readline()
    line = raw_input()
    if line:        
        fr,gst = line.split()
        fr = int(fr)
        if gst!=c:           
            if gst=="waveIn":            
                chnl = (chnl+1)%4
                print "On mixer:",chnl
            elif gst == "waveOut":
                chnl = (chnl-1)%4
                print "On mixer:",chnl
            elif gst =='fist' and not pause:
                pause = True
                s.stop()
            elif pause and gst=="fingersSpread":
                pause = False
                s.start()                
            c = gst            
        mm.setAmp(chnl,0,fr/16.0)
        print spec.lowbound, spec.highbound
            
    else: gst = c            
            
