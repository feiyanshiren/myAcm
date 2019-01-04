for T in range(int(input())):
    b = list(bin(int(input())).replace("0b", ""))
    if b[-1] == "1":
        for i in range(len(b) - 1, -1, -1):
            if b[i] == "1":
                b[i] = "0"
            else:
                break
    print("".join(b))