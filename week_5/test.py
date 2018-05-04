import os
import psutil
import subprocess
from memory_profiler import profile
import time

t=time.time()
p=subprocess.Popen('ipy ps.py 10000', creationflags =subprocess.CREATE_NEW_CONSOLE)
# p=subprocess.call('ipy ps.py 10000', creationflags =subprocess.CREATE_NEW_CONSOLE)
for p in psutil.process_iter(attrs=['pid', 'name']): 
	while True:
		if 'ipy' in p.info['name']:
			pi=p.info['pid']
			print 'overall cpu time:',psutil.Process(pi).cpu_times()
			print 'CPU load: ',psutil.cpu_percent(percpu=True)
			print psutil.Process(pi).memory_info().rss
		else:
			break
print time.time()-t