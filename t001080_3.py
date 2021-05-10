import sys
import ctypes
import platform
sysstr = platform.system()
msvcrt = None
if sysstr == "Windows":
    msvcrt = ctypes.cdll.msvcrt
else:
    msvcrt = ctypes.CDLL("libc.so.6")
n = int(input())
a = [0 for i in range(151)]
for i in range(n):
    k = ctypes.c_int()
    msvcrt.scanf(b"%d", ctypes.byref(k))
    d = int(k.value)
    a[d] = a[d] + 1
for i in range(151):
    for j in range(a[i]):
        sys.stdout.write("%d " % i)
sys.stdout.write("\n")
