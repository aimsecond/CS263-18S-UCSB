from memory_profiler import profile  
@profile(precision=6)
def tim_mea():
	a=[]
	for i in range(2000):
		a.append(i)
	return a
print(tim_mea())
