import os
import psutil
import subprocess
from memory_profiler import profile
import time

t=time.time()
print psutil.cpu_times(percpu=True)
p=subprocess.Popen('pypy binary-trees.py 14', creationflags =subprocess.CREATE_NEW_CONSOLE)
# p=subprocess.call('ipy ps.py 10000', creationflags =subprocess.CREATE_NEW_CONSOLE)
while p:
		try:
			pi=p.pid
			cpu_time=psutil.Process(pi).cpu_times()
			CPU_load=psutil.cpu_percent(percpu=True)
			mem_use=psutil.Process(pi).memory_info().rss
		except:
			print psutil.cpu_times(percpu=True)
			print cpu_time
			print CPU_load
			print mem_use
			break
print time.time()-t