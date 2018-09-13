# 图的研究
def four_direction(vertex_in1, vertex_in2):
    vertex_it1 = list(vertex_in1.values())[0]
    vertex_it2 = list(vertex_in2.values())[0]
    n1 = vertex_it1[0]
    m1 = vertex_it1[1]
    n2 = vertex_it2[0]
    m2 = vertex_it2[1]
    nd = abs(n1 - n2)
    md = abs(m1 - m2)
    d = nd + md
    if d == 1:
        return True
    else:
        return False


def get_distance(vertex_in1, vertex_in2):
    v1 = [int(i) for i in (vertex_in1.split())]
    v2 = [int(i) for i in (vertex_in2.split())]
    n1 = v1[0]
    m1 = v1[1]
    n2 = v2[0]
    m2 = v2[1]
    nd = abs(n1 - n2)
    md = abs(m1 - m2)
    d = nd + md
    return d


"""
def addEdge(G, v1, v2):
    G[v1][v2] = G[v2][v1] = 1
"""


def addEdge(G, v1, v2):
    if v1 not in G[v2]:
        G[v2].append(v1)
    if v2 not in G[v1]:
        G[v1].append(v2)


# dfs1
def dfs1(G, v1, v2, searched=None, path=None):
    if searched is None:
        searched = {}
    if path is None:
        path = []
    searched[v1] = True
    path.append(v1)
    if v1 == v2:
        print("------")
        print(path)
        print("------")
    else:
        for i in G[v1]:
            if i not in searched.keys() or searched[i] is False:
                dfs1(G, i, v2, searched, path)
    path.pop()
    searched[v1] = False


# dfs2
def dfs2(G, v1, v2):
    res = False
    stack = []
    f = G[v1]
    f_map = {}
    for ff in f:
        f_map[ff] = get_distance(ff, v2)
    f_map = sorted(f_map.items(), key=lambda d: d[1], reverse=True)
    f_map = [i[0] for i in f_map]
    stack = stack + f_map
    searched = [v1]
    while len(stack) != 0:
        temp = stack.pop()
        if temp in searched:
            continue
        else:
            searched.append(temp)
            if temp == v2:
                res = True
                print("------")
                print(searched)
                print("------")
            else:
                f = G[temp]
                f_map = {}
                for ff in f:
                    f_map[ff] = get_distance(ff, v2)
                f_map = sorted(f_map.items(), key=lambda d: d[1], reverse=True)
                f_map = [i[0] for i in f_map]
                stack = stack + f_map
    return res


# bfs1
def bfs1(G, v1, v2):
    res = False
    search_list = []
    searched = [v1]
    search_list = search_list + G[v1]
    while search_list != []:
        temp = search_list.pop(0)
        if temp in searched:
            continue
        else:
            searched.append(temp)
            if temp == v2:
                res = True
                print("------")
                print(searched)
                print("------")
                # break
            else:
                search_list = search_list + G[temp]
    return res


# bfs2
def bfs2(G, v1, v2):
    res = False
    search_list = []
    searched = [v1]
    search_list = search_list + G[v1]
    all_path = []
    for i in range(len(G[v1])):
        all_path.append([])
    while search_list != []:
        temp = search_list.pop(0)
        if temp in searched:
            continue
        else:
            searched.append(temp)
            if temp == v2:
                res = True
                break
            else:
                search_list = search_list + G[temp]
    return res


try:
    case = 1
    while True:
        nmh = [int(s) for s in input().split()]
        if len(nmh) == 0:
            continue
        alpha = {}
        maps = []
        hero = []
        vertex = []
        princess = []
        for n in range(nmh[0]):
            one_lines = [s for s in input()]
            for m in range(len(one_lines)):
                one_line = one_lines[m]
                if one_line.isalpha():
                    alpha[one_line] = 0
                if one_line == "@":
                    hero.append(n)
                    hero.append(m)
                if one_line == "*":
                    princess.append(n)
                    princess.append(m)
                if one_line != "#":
                    the_key = "%d %d" % (n, m)
                    vertex.append({the_key: [n, m]})
            maps.append(one_lines)
        for i in alpha.keys():
            A_Z = [s for s in input().split()]
            alpha[A_Z[0]] = A_Z[1] + " " + A_Z[2]
        N = len(vertex)
        # G = [[0] * N for i in range(N)]
        G = {}
        for vertex_in in vertex:
            G[list(vertex_in.keys())[0]] = []
        for n in range(len(vertex)):
            vertex_in1 = vertex[n]
            for m in range(len(vertex)):
                vertex_in2 = vertex[m]
                if four_direction(vertex_in1, vertex_in2):
                    # addEdge(G, n, m)
                    addEdge(G, list(vertex_in1.keys())[0],
                            list(vertex_in2.keys())[0])
        print(maps)
        print(alpha)
        print(hero)
        print(vertex)
        print(G)
        print("==========")
        print(dfs1(G, "%d %d" % (hero[0], hero[1]),
              "%d %d" % (princess[0], princess[1])))
        case = case + 1
except EOFError:
    pass
