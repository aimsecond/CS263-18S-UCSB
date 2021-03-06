import os
import psutil
import subprocess
from memory_profiler import profile
import time

mem_use=0
myinput = open('knucleotide-input.txt')
PERCPU_start=psutil.cpu_times(percpu=True)
t=time.time()
# p=subprocess.Popen('ipy k-nucleotide.ipy',stdin=myinput,creationflags =0)
p=subprocess.Popen('ipy pidigits.ipy 10000',creationflags =0)
pi=p.pid
# p=subprocess.Popen('ipy n-body.ipy 5000000', creationflags =0)
while p.poll()is None:
	try:
		cpu_time=psutil.Process(pi).cpu_times()
		mem_use=max(psutil.Process(pi).memory_info().rss,mem_use)
	except:
		break
print 'Elapsed time: ',time.time()-t
PERCPU_exit=psutil.cpu_times(percpu=True)
print 'CPU time: ',cpu_time.user+cpu_time.system
print 'memory usage: ',str(round(mem_use/1024/1024,2))+' MB'
CPU_load=[]
for i in range(4):
	CPU_load.append(((PERCPU_exit[i].user-PERCPU_start[i].user)/(PERCPU_exit[i].user-PERCPU_start[i].user+PERCPU_exit[i].idle-PERCPU_start[i].idle))*100//1)
print 'CPU_load: ',CPU_load
