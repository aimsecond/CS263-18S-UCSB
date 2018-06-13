import os
import psutil
import subprocess
import time

mem_use=0
myinput = open('knucleotide-input.txt')
PERCPU_start=psutil.cpu_times(percpu=True)
t=time.time()
p=subprocess.Popen('pypy k-nucleotide.py',stdin=myinput,shell = True)
# ===== If program doesn't require an input file ===
# p=subprocess.Popen('python2 fibonacci.py 1200000',shell = True)

pi=p.pid
while p.poll()is None:
	try:
		cpu_time=psutil.Process(pi).cpu_times()
		mem_use=max(psutil.Process(pi).memory_full_info().rss,mem_use)
	except:
		break
print 'Elapsed time: ',time.time()-t
PERCPU_exit=psutil.cpu_times(percpu=True)
print 'CPU time: ',cpu_time.children_user+cpu_time.children_system, cpu_time
print 'memory usage: ',str(round(mem_use/1024,0))+' KB'
CPU_load=[]
for i in range(4):
	CPU_load.append(((PERCPU_exit[i].user-PERCPU_start[i].user)/(PERCPU_exit[i].user-PERCPU_start[i].user+PERCPU_exit[i].idle-PERCPU_start[i].idle))*100//1)
print 'CPU_load: ',CPU_load
