import os
import psutil
import subprocess
from memory_profiler import profile
import time

cpu_time = 0
mem_use = 0
myinput = open('knucleotide-input.txt')

PERCPU_start = psutil.cpu_times(percpu=True)
t=time.time()

p=subprocess.Popen('python2 k-nucleotide.py', stdin=myinput, shell = True)
pi=p.pid


while p.poll() is None:
	cpu_time=psutil.Process(pi).cpu_times()
	mem_use=max(psutil.Process(pi).memory_info().rss,mem_use)
print 'Elapsed time: ',time.time()-t
PERCPU_exit=psutil.cpu_times(percpu=True)
print 'CPU time: ',cpu_time,cpu_time.children_user+cpu_time.children_system
print 'memory usage: ',mem_use,str(round(mem_use/1024,2))+' KB'
CPU_load=[]
for i in range(8):
	CPU_load.append(((PERCPU_exit[i].user-PERCPU_start[i].user)/(PERCPU_exit[i].user-PERCPU_start[i].user+PERCPU_exit[i].idle-PERCPU_start[i].idle))*100//1)
print 'CPU_load: ',CPU_load
# print time.time()-t
# print psutil.cpu_times()
# print CPU_load
# print cpu_time
# print mem_use

# ======================  Old while loop =======================
# while p:
# 		try:
# 			pi=p.pid
# 			cpu_time=psutil.Process(pi).cpu_times()
# 			mem_use=max(psutil.Process(pi).memory_info().rss,mem_use)
# 		except:
# 			print 'Elapsed time: ',time.time()-t
# 			PERCPU_exit=psutil.cpu_times(percpu=True)
# 			print 'CPU time: ',cpu_time.user+cpu_time.system
# 			print 'memory usage: ',str(round(mem_use/1024/1024,2))+' MB'
# 			CPU_load=[]
# 			for i in range(4):
# 				CPU_load.append(((PERCPU_exit[i].user-PERCPU_start[i].user)/(PERCPU_exit[i].user-PERCPU_start[i].user+PERCPU_exit[i].idle-PERCPU_start[i].idle))*100//1)
# 			print 'CPU_load: ',CPU_load
# 			break
# ===========================  close  ===========================
