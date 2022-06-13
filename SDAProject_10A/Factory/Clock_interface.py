from abc import *
import tkinter as Tkinter
import math
from time import strftime
import time	
from interface import *


class watch(Interface):
    def __init__(self):
        pass
    def body(self):
        pass
    def getTime(self):
        pass
    def clk(self):
        pass
    
class analogClock(implements(watch)):
    def __init__(self):
        self.mdl=Tkinter.Tk()
        self.x=150	# Center Point x 
        self.y=150	# Center Point
        self.length=50	# Stick Length
        self.creating_all_function_trigger()
  
	# Creating Trigger For Other Functions
    def creating_all_function_trigger(self):
        self.create_canvas_for_shapes()
        self.body()
        self.dail()
        return

	# Creating Background
    def body(self):
        self.image=Tkinter.PhotoImage(file='clock.gif')
        self.canvas.create_image(150,150, image=self.image)
        return

	# creating Canvas
    def create_canvas_for_shapes(self):
        self.canvas=Tkinter.Canvas(self.mdl, bg='skyblue')
        self.canvas.pack(expand='yes',fill='both')
        return

	# Creating Moving Sticks
    def dail(self):
        self.sticks=[]
        for i in range(3):
            store=self.canvas.create_line(self.x, self.y,self.x+self.length,self.y+self.length,width=2, fill='red')
            self.sticks.append(store)
        return

	# Function Need Regular Update
    def getTime(self):
        now=time.localtime()
        t = time.strptime(str(now.tm_hour), "%H")
        hour = int(time.strftime( "%I", t ))*5
        now=(hour,now.tm_min,now.tm_sec)
		# Changing Stick Coordinates
        for n,i in enumerate(now):
            x,y=self.canvas.coords(self.sticks[n])[0:2]
            cr=[x,y]
            cr.append(self.length*math.cos(math.radians(i*6)-math.radians(90))+self.x)
            cr.append(self.length*math.sin(math.radians(i*6)-math.radians(90))+self.y)
            self.canvas.coords(self.sticks[n], tuple(cr))
        return

    def clk(self):
        while True:
            self.mdl.update()
            self.mdl.update_idletasks()
            self.getTime()
    

class digitalClock(implements(watch)):
    def __init__(self):
        pass
    def body(self):
        window = Tkinter.Tk()
        window.title("")
        window.geometry("200x80")
        window.configure(bg="green")  # =======Background of the clock=====
        window.resizable(False, False)  # =====setting a fixed window size =======

        self.clock_label = Tkinter.Label(
            window, bg="black", fg="cyan", font=("Arial", 30, "bold"), relief="flat"
        )
        self.clock_label.place(x=20, y=20)
        return window
    
    def getTime(self):
        current_time = strftime("%H: %M: %S\n %d-%m-%Y ")
        self.clock_label.configure(text=current_time)
        self.clock_label.after(80, self.getTime)
        self.clock_label.pack(anchor="center")
    
    def clk(self):
        w=self.body()
        self.getTime()
        w.mainloop()