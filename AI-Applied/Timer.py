# Program to demonstrate 
# timer objects in python 

import threading 
import time

def gfg(name): 
    print(name) 
  
timer = threading.Timer(2.0, gfg,("Pic Name",)) 
timer.start() 
print("Exit") 

while (True):
    print(time.perf_counter())



import sched, time
s = sched.scheduler(time.time, time.sleep)

def do_something(sc): 
    print("Doing stuff...")
    # do your stuff
    s.enter(0.2, 1000, do_something, (sc,))

s.enter(0.2, 1000, do_something, (s,))
s.run(True)

print('Take the hole')








