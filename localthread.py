import threading

local_so = threading.local()



def process_so():
    
    var = local_so.var
    print('Here is processing thread (%s) with var %s' %(threading.current_thread().name, var))

def process_thread(tvar):

    local_so.var = tvar
    process_so()


if __name__ == '__main__':
    t1 = threading.Thread(target=process_thread, args=('t1_var',))
    t2 = threading.Thread(target=process_thread, args=('t2_var',))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
