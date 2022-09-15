import time

def function1(endtime):
    init = time.time()
    while True:
        if (time.time()-init) > endtime:
            break
        for i in range(3):
            if (time.time()-init) > endtime:
                break
            print(1)
            time.sleep(1)
        if (time.time()-init) > endtime:
            break
        print(0)
        time.sleep(1)

def function2(endtime):
    num = 50
    init = time.time()
    while num<=100:
        if (time.time()-init) > endtime:
            break
        print(num)
        time.sleep(2)
        num += 2
