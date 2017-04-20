#!/usr/bin/python
import time
from datetime import datetime

#now=time.clock()
with open("natasa.txt", "w") as text_file:
    text_file.write( time.strftime("%H:%M:%S"))
    
    

