import os
import psutil
import subprocess
import time

cpu_time = 0
mem_use = 0
java_time = 0
java_mem = 0
# myinput = open('regexdna-input.txt')

PERCPU_start = psutil.cpu_times(percpu=True)
t=time.time()

# p=subprocess.Popen('jython regex-dna.jython', stdin=myinput, shell = True)
p=subprocess.Popen('python2 binary-trees.py 16', shell = True)
pi=p.pid
while p.poll()is None:
	try:
		cpu_time=psutil.Process(pi).cpu_times()
		mem_use=max(psutil.Process(pi).memory_full_info().rss,mem_use)
	except:
		break
############
# java_pid = -1
# while True:
# 	for pro in psutil.process_iter(attrs=['pid', 'name']):
# 		if pro.info['name'] == "java":
# 			java_pid=pro.info['pid']
# 			break
# 	if java_pid is not -1:
# 		break

# while p.poll()is None:
# 	try:
# 		cpu_time=psutil.Process(pi).cpu_times()
# 		mem_use=max(psutil.Process(pi).memory_info().rss,mem_use)
# 		java_time=psutil.Process(java_pid).cpu_times()
# 		java_mem=max(psutil.Process(java_pid).memory_info().rss,java_mem)
# 		print(cpu_time,mem_use,java_time,java_mem)
# 	except:
# 		break
############
# p.wait()
print 'Elapsed time: ',time.time()-t
PERCPU_exit=psutil.cpu_times(percpu=True)
print 'CPU time: ',cpu_time.children_user+cpu_time.children_system
print 'memory usage: ',str(round(mem_use/1024,0))+' KB'
CPU_load=[]
for i in range(8):
	CPU_load.append(((PERCPU_exit[i].user-PERCPU_start[i].user)/(PERCPU_exit[i].user-PERCPU_start[i].user+PERCPU_exit[i].idle-PERCPU_start[i].idle))*100//1)
print 'CPU_load: '+str(CPU_load)
