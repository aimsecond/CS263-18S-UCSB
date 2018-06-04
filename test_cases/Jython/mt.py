from time import clock
from threading import Thread

N = 5000000

result = []

def f(start, stop):
  result.append(sum(xrange(start, stop)))

threads = [Thread(target=f, args=(i * N, (i + 1) * N)) for i in xrange(10)]

t = clock()

for thread in threads:
  thread.start()

for thread in threads:
  thread.join()

print clock() - t
print sum(result)