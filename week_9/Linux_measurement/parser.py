import os

dir_path = os.path.dirname(os.path.realpath(__file__))

prog_dict = {}
listfile = os.path.join(dir_path,'program_list.txt')
with open(listfile) as f:
    for line in f:
        if line[0] == '#':
            program_type = line[1:-1]
        elif not line[:-1] in prog_dict:
            prog_dict[line[:-1]] = [program_type]
        else:
            prog_dict[line[:-1]].append(program_type)

print prog_dict
csvfile = os.path.join(dir_path,'output.csv')
with open(csvfile,'a') as file:
    for key,value in prog_dict.items():
        file.write(key)
        for i in value:
            file.write(','+i+',')
            f_read =  open(os.path.join(dir_path,'1st_local',i,key),'r')
            data = f_read.readlines()
            elapsed_time = data[-4].split()[2]
            CPU_time = data[-3].split()[2]
            memory_usage = data[-2].split()[2]
            if data[-2].split()[3] == 'MB':
                memory_usage = float(memory_usage)*1024
                memory_usage = str(memory_usage)
            CPU_load = data[-1][12:-2].split()
            f_read.close()
            file.write(elapsed_time+','+CPU_time+','+memory_usage+','+''.join(CPU_load))
            print("finish: "+key+'/'+i)
        file.write('\n')