from guppy import hpy
from memory_profiler import profile

h = hpy()
print(h.heap())

# print(h.heap().byid[0].sp)

# print(h.iso(1,[],{}))

@profile
def d():
    a = "1aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    for i in range(123456):
        a += "1"
    print(a)
    
d()