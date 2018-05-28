import os

listpath = r'/home/haowen/Desktop/CS263-18S-UCSB/week_9/parse_data/'
id_dict={}

# get all .out files and put them to a dictionary
with open(r'/home/haowen/Desktop/CS263-18S-UCSB/week_9/parse_data/file_list.txt') as f:
    for line in f:
        if line[0] == '#':
            program_type = line[1:-1]
            id_dict[program_type] = []
        elif not program_type in id_dict:
            id_dict[program_type] = []
        else:
            id_dict[program_type].append(line[:-1])
    print(id_dict)

# parse the .out files and out put to a .csv file
csvfile = os.path.join(listpath,'output.csv')

with open(csvfile,'a') as file:
    for key,value in id_dict.items():
        for i in value:
            file.write(key + '_' + i)
            f_read =  open(os.path.join(listpath,key,i),'r')
            data = f_read.readlines()
            elapsed_time = data[-4].split()[2]
            CPU_time = data[-3].split()[2]
            memory_usage = data[-2].split()[2]
            CPU_load = data[-1][12:-2].split()
            f_read.close()
            file.write(','+elapsed_time+','+CPU_time+','+memory_usage+','+''.join(CPU_load)+'\n')
            print("finish"+key+i)