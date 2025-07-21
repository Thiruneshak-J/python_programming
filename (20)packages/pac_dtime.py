import time as t
print(t.time())
#t.sleep(2)
print("paused for 2 seconds")
print(t.localtime())
print(t.gmtime())
s=t.perf_counter()
e=t.perf_counter()
print("exceution time",e-s)