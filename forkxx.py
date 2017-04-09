import os
print('Process (%s) start...' %os.getpid())

pid = os.fork()
if pid == 0:
    print('I\'m a child process %s, ppid is %s.' %(os.getpid(), os.getppid()))
else:
    print('I (%s) created a child process (%s)' %(os.getpid(), pid))
