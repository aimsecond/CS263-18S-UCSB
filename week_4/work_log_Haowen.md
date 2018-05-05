# Week_4 Pypy without JIT on Linux Work Log

After installed all required environments, we are going to measure pypy (without JIT) performance.

**About Test_program**

All the test programs have already included in the folder [test_cases](./test_cases)
But these programs are written by other people and thanks to their work, we could utilize these program directly and many works can be saved.
A complete list of these programs can be found at [benchmarksgame](https://benchmarksgame-team.pages.debian.net/benchmarksgame/measurements/python3.html) and [pybenchmarks](https://pybenchmarks.org/u64q/python.php).

To be more specific, here are the links to the detailed description of each program:

[binary-trees](https://pybenchmarks.org/u64q/benchmark.php?test=binarytrees&lang=python&id=1&data=u64q)

[chameneos-redux](https://pybenchmarks.org/u64q/program.php?test=chameneosredux&lang=python&id=1)

[fannkuch-redux](https://pybenchmarks.org/u64q/benchmark.php?test=fannkuchredux&lang=python&id=1&data=u64q)

[fasta](https://pybenchmarks.org/u64q/benchmark.php?test=fasta&lang=python&id=1&data=u64q)

[k-nucleotide](https://pybenchmarks.org/u64q/program.php?test=knucleotide&lang=python&id=1)

[mandelbrot](https://benchmarksgame-team.pages.debian.net/benchmarksgame/program/mandelbrot-python3-7.html)

[meteor-contest](https://pybenchmarks.org/u64q/program.php?test=meteor&lang=pypy&id=3)

[n-body](https://pybenchmarks.org/u64q/program.php?test=nbody&lang=pypy&id=1)

[pidigits](https://pybenchmarks.org/u64q/benchmark.php?test=pidigits&lang=pypy&data=u64q)

[regex-dna](https://pybenchmarks.org/u64q/program.php?test=regexdna&lang=pypy&id=5)

[reverse-complement](https://pybenchmarks.org/u64q/benchmark.php?test=revcomp&lang=pypy&id=3&data=u64q)

[spectral-norm](https://pybenchmarks.org/u64q/program.php?test=spectralnorm&lang=pypy&id=8)

[thread-ring](https://pybenchmarks.org/u64q/program.php?test=threadring&lang=pypy&id=1)

We should notice that the program about are specifically modified for only pypy interpreter.
