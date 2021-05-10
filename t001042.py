def inset_data(the_index, to_index, the_list):
    b = the_list.pop(the_index)
    the_list.insert(to_index, b)
    return the_list


t = int(input())
for i in range(t):
    n = int(input())
    s = [int(j) for j in input().split()]
    s2 = []
    k = 0
    for j in range(n - 1):
        if s[j] != s[j + 1] - 1:
            if k == 0:
                s2.append(s[j])
            else:
                k = 0
        else:
            k = 1
    s1 = s2.copy()
    s1.sort()
    n = len(s2)
    cnt = 0
    i = 0
    while n != 0:
        if s2[0] != s1[0]:
            cnt = cnt + 1
            k = s2.index(s1[0])
            s2 = inset_data(k, 0, s2)
        n = n - 1
        s2.pop(0)
        s1.pop(0)
    print(cnt)
