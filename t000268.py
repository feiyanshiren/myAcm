for n in range(int(input())):
    s = input()
    r = s.count("R")
    w = s.count("W")
    b = s.count("B")
    for i in range(r): print("R", end="")
    for i in range(w): print("W", end="")
    for i in range(b): print("B", end="")
    print()
