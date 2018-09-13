import sys
import heapq
n = int(input())
lst = []
[heapq.heappush(lst, int(i)) for i in input().split()]
for i in range(n):
    sys.stdout.write("%d " % heapq.heappop(lst))
sys.stdout.write("\n")
