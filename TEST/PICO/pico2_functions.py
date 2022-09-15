import time
from random import *

def function3(endtime):
    init = time.time()
    while True:
        looptime = time.time()
        while(time.time()-looptime)<=5 and (time.time()-init)<endtime:
            print(time.time()-looptime)
            print(1)
            time.sleep(0.1)
        while(time.time()-looptime)>=5 and (time.time()-looptime)<=10 and (time.time()-init)<endtime:
            print(time.time()-looptime)
            print(0)
            time.sleep(0.1)
        if(time.time() - init)>endtime:
            break

def function4(endtime):
    init = time.time()
    while True:
        if(time.time() - init)>endtime:
            break
        print(randint(0,100))
        time.sleep(0.1)
