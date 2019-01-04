s = input()
J = 0
O = 0
I = 0
N = 0
T = 0
W = 0
for i in s:
    if i == "J":
        J += 1
    elif i == "O":
        O += J
    elif i == "I":
        I += O
    elif i == "N":
        N += I
    elif i == "T":
        T += N
    elif i == "W":
        W += T
print(W)