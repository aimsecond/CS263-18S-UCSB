# Worklog for Week 4 on Windows

The plan in this week is measuring the performance of PyPy using several test cases.
We find our test programs for PyPy on [pybenchmarks](https://pybenchmarks.org) 
and [benchmark game](https://benchmarksgame-team.pages.debian.net/benchmarksgame/compare/python.html), 
Thanks to their effort, we can use some of the programs directly and make the rest apply for PyPy with a little modification.
All the cases are now executable with PyPy on Windows. 

To measure the performance of PyPy. We have to use several package tools, to measure the program user time,
we simply use the time package and time the program. To measure the memory use of the program, 
we find [memory_profiler](https://pypi.org/project/memory_profiler/) is a useful package, but to use it on windows,
we have to install [psutil](https://psutil.readthedocs.io/en/latest/) package first. 
We experienced a lot difficult in installing the psutil package for PyPy on windows.
After the packages needed are installed we can easily measure the memory usage of a PyPy program. 
The CPU usage is also measured with psutil, fortunately, we have installed it for PyPy and we can directly use it now.

After all the packages installed, we still have to modify the program codes to utilize these packages.