from pyo import *
import sys
import wx




c = ""
pause = False

s = Server().boot()
s.start()

sf = SfPlayer("M.aiff", speed=1, loop=True)
sss = SfPlayer("M.aiff", speed=1, loop=True)
a = FourBand(sf, freq1=500, freq2=800, freq3=1200, mul=.8)
mm = Mixer(outs=4, chnls=4, time = 0.025)
mm.addInput(0,a[1]);mm.addInput(1,a[2]);mm.addInput(2,a[3]);mm.addInput(3,a[4])
mm.setAmp(0,0,0.5);mm.setAmp(1,0,0.5);mm.setAmp(2,0,0.5);mm.setAmp(3,0,0.5)
chnl = 0
amp1 = 0; amp2 = 0; amp3 = 0; amp4 = 0;


#scope1 = Scope(mm[0])

##        scope2 = Scope(mm[1])
##        scope3 = Scope(mm[2])
##        scope4 = Scope(mm[3])
## gui1 = PyoGuiScope(panel)
##gui1.setAnalyzer(scope1)
b = True
while True:    
    mm.out()
    fl = open("DATA.txt","r")
    fl2 = open("DATA2.txt","w")
    line = fl.readline()
    if line and len(line)>1:        
        fr,gst = line.split()
        fr = int(fr)
        if gst!=c:           
            if gst=="waveIn":            
                chnl = (chnl+1)%4
                print "On mixer:",chnl+1
            elif gst == "waveOut":
                chnl = (chnl-1)%4
                print "On mixer:",chnl+1
            elif gst =='fist' and not pause:
                pause = True
                s.stop()
            elif pause and gst=="fingersSpread":
                pause = False
                s.start()                
            c = gst            
        mm.setAmp(chnl,0,fr/16.0)
        if chnl == 0:
            amp1 = fr
        elif chnl == 1:
            amp2 = fr
        elif chnl == 2:
            amp3 = fr
        else:
            amp4 = fr
                
        fl2.write(" ".join(map(str,[amp1,amp2,amp3,amp4,chnl])))      
            
    else: gst = c            
  

