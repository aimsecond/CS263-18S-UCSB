
# CS263-18S-UCSB
The repository for uploading UCSB [CS263: Runtime System](http://www.cs.ucsb.edu/~cs263/index.html) code. This readme is basically a copy of our project vision, but progress will be updated regularly.

---
**Project progress**

Week 2: Determine which topic to choose, finish project vision **[Finished]**

 - [x] [project vision](week_2/Project%20Vision.md)

Week 3: Download these interpreter. Learn how to use different interpreters
Week 4: Pypy performance measurement
Week 5: IronPython performance measurement
Week 6: PyPy/JIT performance measurement
Week 7: CPython performance measurement
Week 8: Jython performance measurement
Week 9: Compare these performance and produce the report
Week 10: Presentation

---
**Project Member**
![Alt text](week_2/Chang%20Lu.JPG?raw=true "Title")
Chang Lu [Email](changlu@umail.ucsb.edu)
![Alt text](week_2/Haowen%20Zhang.JPG?raw=true "Title")
Haowen Zhang [Email](haowen@ucsb.edu)

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
