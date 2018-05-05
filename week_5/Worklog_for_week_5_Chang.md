# WorkLog for week 5
- Complete the code submitted last week
We submit the test case last week for PyPy, and all the code can be run in
the command line, but we did not finish the work of measurement. We have
modified the code we submitted. Now when execute the code it will report
the user time, CPU time, memory usage and CPU load, these measures are
supported by psutil and memory_profiler module. 

- IronPython Progress
As the project vision, we are supposed to work on IronPython this week, I
tried to make IronPython work by installing the same packages I used in
PyPy, Unfortunately, most of them does not work, because pip is a new
module in IronPython, it can only support a few packages, what we need are
all not available in IronPython. 
I tried to find other alternatives to profile the resource usage of IronPython
application, there is a built-in package in IronPython which can monitor the
resource usage. However, it is only available in unix OS, and we had lots of
difficult in built IronPython on Ubuntu last week, and finally gave up.
Therefore I have to find another way.
By learning the method used in [pybenchmark](https://pybenchmarks.org/play.php),I decide to use subprocess 
package built-in Python, this module is used to manage subprocess from a
Python scripts, and return the usage info of the child-process. In this way, I
can execute IronPython and assigned the measurement task to CPython
which supports lots of modules including psutil.

- Issues needs to be solve:
We have successfully measure the performance of one of the IronPython program,
but still have more work to do with other programs, we have to find similar program 
as mentioned in project vision. However, there are many packages that IronPython does 
not support, So There will be some programs that has no alternative in IronPython. 