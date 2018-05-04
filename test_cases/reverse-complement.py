# The Computer Language Benchmarks Game
# http://benchmarksgame.alioth.debian.org/
# 
# contributed by Jacob Lee, Steven Bethard, et al
# 2to3
# fixed by Daniele Varrazzo

from __future__ import print_function
import sys, string

import time
from memory_profiler import profile
import psutil
import os

def show(seq, 
         table=string.maketrans(b'ACBDGHK\nMNSRUTWVYacbdghkmnsrutwvy',
                                b'TGVHCDM\nKNSYAAWBRTGVHCDMKNSYAAWBR')):
                                
   seq = (''.join(seq)).translate(table)[::-1]
   for i in range(0, len(seq), 60):
      print(seq[i:i+60])
      
@profile
def main():
   seq = []
   add_line = seq.append
   for line in sys.stdin:
      if line[0] in '>;':
         show(seq)
         print(line, end='')
         del seq[:]
      else:
         add_line(line[:-1])
   show(seq)

t=time.time()
main()
print 'user time: ',time.time()-t
print 'overall cpu time:',psutil.Process(os.getpid()).cpu_times()
print 'CPU load: ',psutil.cpu_percent(percpu=True)
print 'overall cpu times: ',psutil.cpu_times()