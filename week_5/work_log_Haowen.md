# Week_5 IronPython on Linux Work Log

Because IronPython very difficult to be installed on the Ubuntu OS, this week I put most of the time figuring out how to install IronPython to Ubuntu.

I have also downloaded test programs for ironPython. Here are the detailed description:

[n-body](https://pybenchmarks.org/u64q/program.php?test=nbody&lang=ipy&id=1)

[thread-ring](https://pybenchmarks.org/u64q/program.php?test=threadring&lang=ipy&id=1)

[richards](https://pybenchmarks.org/u64q/program.php?test=richards&lang=ipy&id=1)

[pystone](https://pybenchmarks.org/u64q/program.php?test=pystone&lang=ipy&id=1)

[fibonacci](https://pybenchmarks.org/u64q/program.php?test=fibonacci&lang=ipy&id=3)

[k-nucleotide](https://pybenchmarks.org/u64q/program.php?test=knucleotide&lang=ipy&id=1)

[regex-dna](https://pybenchmarks.org/u64q/program.php?test=regexdna&lang=ipy&id=5)

[spectral-norm](https://pybenchmarks.org/u64q/program.php?test=spectralnorm&lang=ipy&id=8)

[pidigits](https://pybenchmarks.org/u64q/program.php?test=pidigits&lang=ipy&id=1)

What's more, we decided to change the method for measuring the cpu time, memory usage,etc. This is because the pip packages we used to measure these data are not 
supported in the IronPython, so we decide to switch to another method: use the python built-in functions to measure these data.

Beside the work above, I am writing a script that enable us to measure these test program automatically.