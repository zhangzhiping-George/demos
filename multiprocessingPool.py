#!/usr/bin/env python
from multiprocessing import Pool
import os, time, random

def pool_proc(name):
    print('running proc (%s)in Pool' %os.getid())
    start = time.time()
    time.sleep(random.random()*2)
    end = time.time()
    print('Task %s cost time: %s' %(name, (end - start)))

if __name__ == '__main__':

    print('Parent id %s' %os.getpid())
    p = Pool(4)
    for i in range(3):
        print('i:%s' %i)
        p.apply_async(pool_proc, args=(i,))
    print('Waiting...')
    p.close()
    p.join
    print('Over')
