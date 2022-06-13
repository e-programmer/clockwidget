from abc import *
import tkinter as Tkinter
import math
from time import *
import time	
   
class watchTemp(ABC):
    
    def __init__(self):
        self.flag= None
    def getTime(self):
        pass
    @abstractmethod
    def body(self):
        pass
    def dail():
        pass
    def clk(self):
        if self.flag == False: 
            w=self.body()
            self.getTime()
            w.mainloop()
        
        else:
            while True:
                self.mdl.update()
                self.mdl.update_idletasks()
                self.getTime()

#--------------------------------------------ANALOG CLOCK--------------------------- 
class analogClock(watchTemp):
    
	def __init__(self):
		watchTemp.__init__ (self)
		self.flag= True
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

   
#------------------------------------------DIGITAL CLOCK----------------------------------
class digitalClock(watchTemp):
    def __init__(self):
        watchTemp.__init__ (self)
        self.flag= False
    
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
    
#-----------------------MAIN----------------------------------------
if __name__ == '__main__':
    d=digitalClock()
    # print(d.flag)
    d.clk()
    # a=analogClock()
    # print(a.flag)
    # a.clk()   