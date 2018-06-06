import os
import psutil
import subprocess
import time
import multiprocessing
from sys import platform

cpu_corenumber = multiprocessing.cpu_count()
current_dir_path = os.path.dirname(os.path.realpath(__file__))

def get_proglist_by_progname():
    prog_dict = {}
    listfile = os.path.join(current_dir_path,'Instruction.txt')
    with open(listfile) as f:
        for line in f:
            if line[0] == '#':
                program_type = line[1:-1]
            elif not line[:-1] in prog_dict:
                prog_dict[line[:-1]] = [program_type]
            else:
                prog_dict[line[:-1]].append(program_type)
    return prog_dict

def get_proglist_by_interpreter():
    interpreter_dict = {}
    listfile = os.path.join(current_dir_path,'Instruction.txt')
    with open(listfile) as f:
        for line in f:
            if line[0] == '#':
                interpreter_type = line[1:-1]
            elif not interpreter_type in interpreter_dict:
                interpreter_dict[interpreter_type] = [line[:-1]]
            else:
                interpreter_dict[interpreter_type].append(line[:-1])
    return interpreter_dict

#for name consistency
def folder_name_modifier(name):
    try:
        if name == 'python':
            return 'CPython'
        elif name == 'jython':
            return 'Jython'
        elif name == 'ironpython':
            return 'IronPython'
        elif name == 'pypy':
            return "PyPy"
        else:
            raise ValueError('name wrong. Check your proglist')
    except ValueError as err:
        print(err.args)
        
def run_program(interpreter,programname,parameter,filepath):
    runprogramname = os.path.join(filepath,programname)
    outputfilepath = os.path.join(current_dir_path,folder_name_modifier(interpreter))
    if not os.path.exists(outputfilepath):
        try:
            os.makedirs(outputfilepath)
        except:
            print("Error creating output file path: "+programname) 
    

    mem_use = 0
    t = 0
    PERCPU_start = 0
    java_time = 0
    java_mem = 0
    CPU_time = 0

    if interpreter != "jython":
        if parameter[-3:] == "txt":
            myinput = open(os.path.join(filepath,parameter))
            PERCPU_start = psutil.cpu_times(percpu=True)
            t=time.time()
            p=subprocess.Popen(interpreter+' '+runprogramname, stdin=myinput, shell = True)
        else:
            PERCPU_start = psutil.cpu_times(percpu=True)
            t=time.time()
            p=subprocess.Popen(interpreter+' '+runprogramname+' '+parameter, shell = True)
        pi=p.pid
        
        while p.poll()is None:
            cpu_time=psutil.Process(pi).cpu_times()
            mem_use=max(psutil.Process(pi).memory_info().rss,mem_use)
    
        elapsed_time = 	str(time.time()-t)
        PERCPU_exit=psutil.cpu_times(percpu=True)
        memory_usage = str(round(mem_use/1024,0))+' KB'
        CPU_load=[]
    else:
        if parameter[-3:] == "txt":
            myinput = open(os.path.join(filepath,parameter))
            PERCPU_start = psutil.cpu_times(percpu=True)
            t=time.time()
            p=subprocess.Popen(interpreter+' '+runprogramname, stdin=myinput, shell = True)
        else:
            PERCPU_start = psutil.cpu_times(percpu=True)
            t=time.time()
            p=subprocess.Popen(interpreter+' '+runprogramname+' '+parameter, shell = True)
        pi=p.pid
        java_pid = -1
        while True:
        	for pro in psutil.process_iter(attrs=['pid', 'name']):
        		if pro.info['name'] == "java":
        			java_pid=pro.info['pid']
        			break
        	if java_pid is not -1:
        		break
        
        while p.poll()is None:
        	try:
        		cpu_time=psutil.Process(pi).cpu_times()
        		mem_use=max(psutil.Process(pi).memory_info().rss,mem_use)
        		java_time=psutil.Process(java_pid).cpu_times()
        		java_mem=max(psutil.Process(java_pid).memory_info().rss,java_mem)
        	except:
        		break
    
        elapsed_time = 	str(time.time()-t)
        PERCPU_exit=psutil.cpu_times(percpu=True)
        memory_usage = str(round((mem_use+java_mem)/1024,0))+' KB'
        CPU_load=[]
        CPU_time = java_time.user+java_time.system

    if platform == "win32":
        CPU_time = cpu_time.user+cpu_time.system
    elif platform == "linux" or platform == "linux2":
        CPU_time = CPU_time + cpu_time.children_user+cpu_time.children_system
        if CPU_time == 0.0:
            return False
    for i in range(cpu_corenumber):
        if PERCPU_exit[i].user-PERCPU_start[i].user+PERCPU_exit[i].idle-PERCPU_start[i].idle == 0.0:
            CPU_load.append(0.0)
        else:
            CPU_load.append(((PERCPU_exit[i].user-PERCPU_start[i].user)/(PERCPU_exit[i].user-PERCPU_start[i].user+PERCPU_exit[i].idle-PERCPU_start[i].idle))*100//1)

    outputfile = os.path.join(outputfilepath,programname.split('.')[0]+'.out')
    print outputfile
    with open(outputfile,'w') as file:
        file.write('Elapsed time: '+elapsed_time+'\n')
        file.write('CPU time: '+ str(CPU_time)+'\n')
        file.write('memory usage: '+memory_usage+'\n')
        file.write('CPU_load: '+ str(CPU_load)+'\n')
    return True

def main():
    proglist = get_proglist_by_interpreter()
    print proglist
    for key,value in proglist.items():
        filepath = os.path.join(os.path.dirname(os.path.dirname(current_dir_path)),'test_cases',key)
        interpreter = key.lower()
        if interpreter == 'cpython':
            interpreter = 'python'
        elif interpreter == 'ironpython':
            interpreter = 'ipy'
        for i in value:
            programname = i.split(',')[0]
            parameter = i.split(',')[1]
            print(interpreter,programname,parameter,filepath+"\n")
            while not run_program(interpreter,programname,parameter,filepath):
                continue
            
        
    
if __name__ == '__main__':
    main()