import Clock_interface
from abc import *

class ClockCreator(ABC):
    @abstractmethod
    def createClock(self):
        pass
    def render(self):
        #mywatch= Clock_interface.watch()
        product= self.createClock()
        product.clk()
    
class analogClockCreator(ClockCreator):
    def createClock(self):
        aC= Clock_interface.analogClock()
        return aC
    
class digitalClockCreator(ClockCreator):
    def createClock(self):
        dC= Clock_interface.digitalClock()
        return dC           