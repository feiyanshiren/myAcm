n = 0
a = []
k = 0
def dfs(i, su):
    global n
    global k
    global a
    if i == n:
        return su == k
    if dfs(i + 1, su):
        return True
    if dfs(i + 1, su + a[i]):
        return True
    return False
try:
    while 1:
        s = [int(i) for i in input().split()]
        n = s[0]
        k = s[1]
        a = [int(i) for i in input().split()]
        print("YES") if dfs(0, 0) else print("NO")
except:
    pass
