# Week_3 Linux Work Log

After discussed with ChangLu, we decided to test those different python interpreters on different platforms
I will test them on a linux machine, with 1GB memory and a Intel(R) Xeon(R) CPU @ 2.50GHz Cpu
>$ cat /proc/cpuinfo
>>model name: Intel(R) Xeon(R) CPU @ 2.50GHz

>$ lscpu
>>Architecture:          x86_64
CPU op-mode(s):        32-bit, 64-bit
Byte Order:            Little Endian
CPU(s):                8
On-line CPU(s) list:   0-7
Thread(s) per core:    2
Core(s) per socket:    4
Socket(s):             1
NUMA node(s):          1
Vendor ID:             GenuineIntel
CPU family:            6
Model:                 62
Stepping:              4
CPU MHz:               2499.998
BogoMIPS:              4999.99
Hypervisor vendor:     KVM
Virtualization type:   full
L1d cache:             32K
L1i cache:             32K
L2 cache:              256K
L3 cache:              30720K
>>NUMA node0 CPU(s):     0-7

## Time line
**Apr.15**
1. Created a ubunutu based container in [Cloud9](https://ide.c9.io/aimsecond/cs263-18s-ucsb) as one of our test environment
2. Installed pypy on the ubuntu container.

**Apr.19**
1. Installed pypy on the ubuntu container
>$ pypy --version
>>[PyPy 5.10.0 with GCC 6.2.0 20160901]
2. Have problem on installing ironpython on ubuntu container
- required dot net CLI
- after installing dot CLI, we used 'msbuild' to build .exe out of IronPython.sln file
- build is not successful
- possible solution: [artical1](https://stackoverflow.com/questions/45664694/instaling-ironpython-for-linux) / build .exe in windows first, then copy it to ubuntu
3. Installed Cython on the container
>$ cython --version
>>Cython version 0.28

**Apr.20**
1. Installed Jython on the ubuntu container
>$ jython --version
>>Jython 2.7.0