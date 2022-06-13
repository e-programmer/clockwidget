from interface import *
import Clocks

class watches(Interface):
    def __innit__(self):
        pass
    def DisplayAnalogClock(self):
        pass
    def DisplayDigitalClock(self):
        pass
    
class watchAdapter(implements(watches)):
    def __innit__(self):
        pass
    def DisplayAnalogClock(self):
        ac=Clocks.analogClock()
        ac.clk()
    def DisplayDigitalClock(self):
        dc=Clocks.digitalClock()
        dc.clk()
        
if __name__ == '__main__':
# class main:
    # a=watchAdapter()
    # a.DisplayAnalogClock()
    
    d=watchAdapter()
    d.DisplayDigitalClock()