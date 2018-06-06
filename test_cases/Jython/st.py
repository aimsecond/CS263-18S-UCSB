from time import clock
from threading import Thread

N = 5000000
t = clock()
print sum(xrange(N * 10))
print clock() - t