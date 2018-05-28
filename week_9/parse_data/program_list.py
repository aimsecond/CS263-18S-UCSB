import os

prog_dict = {}
with open(r'/home/haowen/Desktop/CS263-18S-UCSB/week_9/parse_data/file_list.txt') as f:
    for line in f:
        if line[0] == '#':
            program_type = line[1:-1]
        elif not line[:-5] in prog_dict:
            prog_dict[line[:-5]] = [program_type]
        else:
            prog_dict[line[:-5]].append(program_type)
# print(prog_dict)
for key in prog_dict:
    print(key,prog_dict[key])
