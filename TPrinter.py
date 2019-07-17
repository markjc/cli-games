from time import sleep
import sys

class TPrinter:
    
    def __init__(self):
        #Initialization Function - Set Default Seconds
        self.default_seconds = 0.08
        
    def tprint(self, text, seconds=None):
        
        if seconds == None:
            seconds = self.default_seconds
            
        #Print the supplied text, with the seconds variable as the interval.
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(seconds)