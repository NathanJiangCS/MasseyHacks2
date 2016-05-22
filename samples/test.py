from pyo import *
s = Server().boot()
s.start()
sf = SfPlayer("M.aiff", speed=1, loop=True)
spec = Spectrum(sf, size=1024)
spec.polltime(1)
spec.poll(True)
print spec.highbound
