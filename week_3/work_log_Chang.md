#Week 3 Windows worklog
##Environment Setup
###Installing PyPy on Windows
-	Download the windows version PyPy(with JIT) from [PyPy](https://PyPy.org/download.html)
-	Download VS 2008 runtime library installer and install
-	Unzip zip file to local
-	Add the direction of PyPy.exe to the Environment Variables

**Test PyPy with test case :**
Use command:
>PyPy test.py

the result is:
>0.111999988556

**For PyPy without JIT:**
Use command: 
>PyPy --jit off test.py

the result is:
>10.7279999256

###Installing IronPython on Windows
-	Download IronPython2.7.8 from [IronPython](http://ironpython.net/)
-	Unzip zip file to local
-	Add the direction of ipy.exe to the Path in Environment Variables

**Test IronPython with test case**
Use command:
>ipy test.py

the result is:
>1.53894805908

###Installing Jython on Windows
-	Download the installer from [Jython](http://www.jython.org/downloads.html)
-	Install Jython with command java -jar jython-installer-2.7.0.jar
-	Select the standard Jython
-	Add the direction of jython.exe to the System Path

**Test Jython with test case**
Use command:
>jython test.py

the result is:
>4.01799988747

###Installing Cython on Windows
-	Installing Python2.7 on Windows
-	Add the direction of Python2.7 to Environment Variables
-	Download get-pip.py
-	Installing pip with command python get-pip.py and python -m install –upgrade pip
-	Installing Cython with command pip install Cython

**Test Cython with test case:**
>cython test.py

Create a test.c file, In the file is a failed record for using Cython.

**To use Cython:**
-	Create a *.pyx file rather than a .py file
-	Create a setup.py to build
-	Use python setup.py build_ext –inplace to compile *.pyx
-	Then there will be a *.c and *.so
-	Import the .so file and call the function in *.pyx
Then the Cython will work

##Test
Test.py is a loop and Print the time of Running the loop

##Documentation
[CPython](https://docs.python.org/2/)
1.	CPython is the most widely used implementation of Python, Python2.x and Python3.x are both CPython
2.	CPython is implemented in C

[PyPy](http://doc.PyPy.org/en/latest/index.html)
1.	Use JIT compiler and is faster than CPython is some case where less function is called from other packages. But in other cases where the main time consumption is calling functions from other packages, PyPy perform worse than CPython.
2.	Some large programs take less space in PyPy than in CPython
3.	PyPy comes by default with support for stackless mode, providing micro-threads for massive concurrency
4.	PyPy does not support C extensions very well, for example Numpy
PyPy without JIT
Because the fast speed of PyPy over CPython is brought by JIT compiler, if the JIT of PyPy is turned off, the performance of PyPy will be worse than CPython.

[IronPython](https://docs.python.org/2.7/)
1.	IronPython is an implementation for .NET platform and is implemented in C#
2.	.NET library can be used in an IronPython application and IronPython can be used in C# application.
3.	IronPython supports multi-core better because the lack of GIL
4.	IRonPython has a limited ability to extend C
5.	IronPython support less cross-platform support
6.	IronPython has better performance (in the test case)

[Jython](http://www.jython.org/docs/index.html)
1.	Jython is an implementation for JVM and is implemented in JAVA
2.	Jython application can use JAVA libraries
3.	The time performance of Jython reported is not as good as CPython

[Cython](https://cython.readthedocs.io/en/latest/)
1.	Cython is an implementation in C
2.	Cython has better C extensions, and Cython can use C libraries.
3.	Cython combines the easy use of python and the fast speed of C
4.	Cython has a better performance than CPython