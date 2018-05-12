import os
import psutil
import subprocess
from memory_profiler import profile
import time

print psutil.cpu_times(percpu=True)
t=time.time()
p=subprocess.Popen('python2 binary-trees 15', shell = True)
# pi=p.pid
# mem_use = 0
# while p:
# 	try:
# 		cpu_time=psutil.Process(pi).cpu_times()
# 		mem_use=max(psutil.Process(pi).memory_info().rss,mem_use)
# 	except:
# 		print 'Elapsed time: ',time.time()-t
# 		PERCPU_exit=psutil.cpu_times(percpu=True)
# 		print 'CPU time: ',cpu_time.user+cpu_time.system
# 		print 'memory usage: ',str(round(mem_use/1024/1024,2))+' MB'
# 		CPU_load=[]
# 		for i in range(4):
# 			CPU_load.append(((PERCPU_exit[i].user-PERCPU_start[i].user)/(PERCPU_exit[i].user-PERCPU_start[i].user+PERCPU_exit[i].idle-PERCPU_start[i].idle))*100//1)
# 		print 'CPU_load: ',CPU_load
# 		break

pi=p.pid

cpu_time = 0
mem_use = 0
while p.poll() is None:
	cpu_time=psutil.Process(pi).cpu_times()
	CPU_load=psutil.cpu_percent(percpu=True)
	mem_use=psutil.Process(pi).memory_full_info()
print time.time()-t
print psutil.cpu_times()
print CPU_load
print cpu_time
print mem_use

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
