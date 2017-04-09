from multiprocessing import Process, Queue
import os, time, random

def write(q):
    for info in ['A', 'B', 'C']:
        print('Write %s into Queue: %s (%s)'  %(info, q, os.getpid()))
        q.put(info)
        time.sleep(random.random())

def read(q):
    while True:
        print('Read info from Queue: %s (%s)' %(q, os.getpid()))
        value = q.get()
        print('Value read from queue: %s' %value)


if __name__ == '__main__':
    
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
    
