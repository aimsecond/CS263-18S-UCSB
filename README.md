
# CS263-18S-UCSB
The repository for uploading UCSB [CS263: Runtime System](http://www.cs.ucsb.edu/~cs263/index.html) code. This readme is basically a copy of our project vision, but progress will be updated regularly.

---
**Project progress**

Week 2: Determine which topic to choose, finish project vision **[Finished]**

 - [x] [project vision](./week_2/Project%20Vision.md)

Week 3: Download these interpreter. Learn how to use different interpreters **[Finished]**
 - [x] [work log on Windows environment](./week_3/work_log_Chang.md)
 - [x] [work log on Ubuntu docker environment](./week_3/work_log_Haowen.md)
 - [x] Tested a timer program for each interpreter/compiler

Week 4: [Pypy](https://pypy.org/) performance measurement
 - [x] [work log on Windows environment](./week_4/work_log_ChangLu.md)
 - [x] [work log on Ubuntu docker environment](./week_4/work_log_Haowen.md)
 - [x] All the programs now is ready to run with pypy without errors.
 - [ ] Finish the auto-measurement script for pypy.

Week 5: [IronPython](http://ironpython.net/) performance measurement
 - [ ] Finish the auto-measurement script for IronPython.
 - [ ] Install the IronPython to the Ubuntu environment.

Week 6: [PyPy/JIT](https://pypy.org/) performance measurement

Week 7: [Cython](http://cython.org/) performance measurement

Week 8: [Jython](http://www.jython.org/) performance measurement

Week 9: Compare these performance and produce the report

Week 10: [Presentation](./Presentation/CS263_Haowen%20Zhang_Chang%20Lu.pptx)

---
**Project Member**

Chang Lu [Email](changlu@umail.ucsb.edu)

<img src="./week_2/Chang%20Lu.JPG" width="250">

Haowen Zhang [Email](haowen@ucsb.edu)

<img src="./week_2/Haowen%20Zhang.JPG" width="250">

---
**Project Idea**

Performance comparisons

Python: PyPy, IronPython, PyPy/JIT, CPython, other. Use 5+ real programs you find via github or elsewhere (http://benchmarksgame.alioth.debian.org has some small programs, if you use these, then you need a minimum of 10 programs)

**Interpreters to be compared**

PyPy, IronPython, PyPy/JIT, CPython,Jython.(Other interpreters to be explored later)

**Parameters to be measured**

Overall user runtime, memory usage, compressed source code size, CPU time over all threads, CPU load for each core.

Other parameters might be decided to compare:

(throughput? machine-learning based approaches to performance adaptation?)

**Benchmark Programs**

We are going to start with the programs compared in Benchmark Games and meanwhile find programs on github. We will add them in the benchmark if found. [The programs compared in Benchmark Games](https://en.wikipedia.org/wiki/The_Computer_Language_Benchmarks_Game) including: binary-trees chameneos-redux fannkuch-redux fasta k-nucleotide mandelbrot meteor-contest n-body pidigits regex-redux reverse-complement spectral-norm thread-ring.
