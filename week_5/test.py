import os
import psutil
import subprocess
from memory_profiler import profile
import time

t=time.time()
p=subprocess.Popen('pypy binary-trees.py 14', shell = True)
# p=subprocess.call('ipy ps.py 10000', shell = true)
print p.pid, psutil.Process(p.pid).name()
# for p in psutil.process_iter(attrs=['pid', 'name']): 
# 	while True:
# 		if 'pypy' in p.info['name']:
# 			pi=p.info['pid']
# 			print 'overall cpu time:',psutil.Process(pi).cpu_times()
# 			print 'CPU load: ',psutil.cpu_percent(percpu=True)
# 			print psutil.Process(pi).memory_info().rss #Find a PeakProcessMemoryUsed
# 		else:
# 			break
print time.time()-t