import os
import psutil
import subprocess
import time

# cpu_time = 0
mem_use = 0
# myinput = open('knucleotide-input.txt')

PERCPU_start = psutil.cpu_times(percpu=True)
t=time.time()

# p=subprocess.Popen('python2 k-nucleotide.py', stdin=myinput, shell = True)
p=subprocess.Popen('pypy binary-trees 19', shell = True)
pi=p.pid


while p.poll()is None:
	try:
		cpu_time=psutil.Process(pi).cpu_times()
		mem_use=max(psutil.Process(pi).memory_info().rss,mem_use)
	except:
		break
print 'Elapsed time: ',time.time()-t
PERCPU_exit=psutil.cpu_times(percpu=True)
print 'CPU time: ',cpu_time
print 'memory usage: ',str(round(mem_use/1024,0))+' KB'
CPU_load=[]
for i in range(4):
	CPU_load.append(((PERCPU_exit[i].user-PERCPU_start[i].user)/(PERCPU_exit[i].user-PERCPU_start[i].user+PERCPU_exit[i].idle-PERCPU_start[i].idle))*100//1)
print 'CPU_load: ',CPU_load
