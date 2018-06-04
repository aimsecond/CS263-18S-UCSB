import os
import psutil
import subprocess
import time

mem_use=0
java_pid=0
java_mem = 0
# myinput = open('regexdna-input.txt')
PERCPU_start=psutil.cpu_times(percpu=True)
t=time.time()
# p=subprocess.Popen('jython regex-dna.jython',stdin=myinput,creationflags =0)
p=subprocess.Popen('jython mt.py',creationflags =0)
pi=p.pid
# p=subprocess.Popen('ipy n-body.ipy 5000000', creationflags =0)
while True:
	for pro in psutil.process_iter(attrs=['pid', 'name']):
		if 'java.exe' in pro.info['name']:
			java_pid=pro.info['pid']
			break
	if java_pid:
		break
while p.poll()is None:
	try:
		cpu_time=psutil.Process(pi).cpu_times()
		mem_use=max(psutil.Process(pi).memory_info().rss,mem_use)
		java_time=psutil.Process(java_pid).cpu_times()
		java_mem=max(psutil.Process(java_pid).memory_info().rss,java_mem)
	except:
		break
print 'Elapsed time: ',time.time()-t
PERCPU_exit=psutil.cpu_times(percpu=True)
print 'CPU time: ',cpu_time.user+cpu_time.system+java_time.user+java_time.system
print 'memory usage: ',str(round((mem_use+java_mem)/1024,0))+' KB'
CPU_load=[]
for i in range(4):
	CPU_load.append(((PERCPU_exit[i].user-PERCPU_start[i].user)/(PERCPU_exit[i].user-PERCPU_start[i].user+PERCPU_exit[i].idle-PERCPU_start[i].idle))*100//1)
print 'CPU_load: ',CPU_load
