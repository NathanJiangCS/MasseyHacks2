import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import Tkinter as tk
import ttk



style.use('ggplot')

        
f = Figure(figsize=(10,6), dpi=100)
ax = f.add_subplot(111)

width = [0,0,0,0,0]
lwidth = [0,0,0,0,0]

def animate(i):
    global width,lwidth
    pullData = open('DATA2.txt','r')
    line = pullData.readline().strip(" \n").split()
    yaxes = [0,1,2,3,0]
    start = [0,0,0,0,16]
    colors = ['#f7cac9','#f7cac9','#f7cac9','#f7cac9','#f7cac9']
    
    if line:        
        width = map(float,line)
        chnl = width.pop()
        colors[int(chnl)] = '#eea29a'
        width+=[0]
        for i in xrange(5): lwidth[i] = width[i]        
        
    else:
        for i in xrange(5): width[i] = lwidth[i]
    labels = ['Bass','Sub-Bass','Mid','High']
            
    ax.clear()
    
    ax.barh(bottom = yaxes, width = width, left = start, height = 1,align='center',color=colors)
    ax.set(yticks=yaxes, yticklabels=labels, ylabel='Frequency Bands',xlabel='Output Level')
    ax.xaxis.labelpad = 10; ax.title.labelpad = 20; ax.set_axis_bgcolor("#d5f4e6")
    

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        
        tk.Tk.wm_title(self, "Myusicality")
        
        
        container = tk.Frame(self)
        
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(container, self)
        self.frames[StartPage] = frame
        frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH, expand=True)
         

app = SeaofBTCapp()
ani = animation.FuncAnimation(f,animate,interval=10)
app.mainloop()

    

