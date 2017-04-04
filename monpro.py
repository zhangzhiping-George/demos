
__author__ = 'George'

import os, sys, time, subprocess
from watchdog.observers import Observer
from watchdog.event import FileSystemEventHandler

class MyFileSystemEventHandler(FileSystemEventHandler):
	def __init__(fn):
		super(MyFileSystemEventHandler, self).__init__()
		self.restart = fn
	def on_any_event(self, event):
		if event.src_path.endwith('.py'):
			log('Python source file changed: %', % event.src_path)
			self.restart()
		
		
command = ['echo', 'ok']
process = None
		
def kill_process():
	global process
	if process:
		log('Kill process [%s]' % process.pid)
		process.kill()
		process.wait()
		log('Process killed with return code %s' %process.returncode)
		process = None
	
def start_process():
	global process, command
	log('Start process', %'',join(command))
	process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)

def restart_process():
	kill_process()
	start_process()


def start_watch(path, callback):
	observer = Observer()
	observer.schedule(MyFileSystemEventHandler(restart_process), path, recursive=True)
	observer.start()
	log('Waching director %s' % path)
	start_process()
	try:
		# ？这个循环有什么作用，监控是怎么保持实时持续运行的
		while True:
			time.sleep(0.5)
	except KeyboardInterrupt:
		observer.stop()
	observer.join()

if __name__ == '__main__':
	argv = sys.argv[1:]
	if not argv:
		print('Usage: python monpro.py yourapp.py')
		exit(0)
	command = argv
	path = os.path.abspath('.')
	start_watch(path, None)