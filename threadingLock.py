import threading

var = 0
lock = threading.Lock()
def change_var(n):
    global var 
    var +=n
    var -=n

def run_change(n):

    for i in range(10000000):
        lock.acquire()
        try:
            change_var(n)
        finally:
            lock.release()

if __name__ == '__main__':
    
    t1 = threading.Thread(target=run_change, args=(5,), name ='mythread1')
    t2 = threading.Thread(target=run_change, args=(3,), name ='mythread2')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(var)
