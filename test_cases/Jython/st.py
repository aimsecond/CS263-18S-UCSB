from time import clock
from threading import Thread

N = 50000000
t = clock()
print sum(xrange(N * 10))
print clock() - t