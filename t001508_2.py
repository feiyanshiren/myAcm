m = {
    "a": "2", "b": "2", "c": "2",
    "d": "3", "e": "3", "f": "3",
    "g": "4", "h": "4", "i": "4",
    "j": "5", "k": "5", "l": "5",
    "m": "6", "n": "6", "o": "6",
    "p": "7", "q": "7", "r": "7", "s": "7",
    "t": "8", "u": "8", "v": "8",
    "w": "9", "x": "9", "y": "9", "z": "9",
    " ": "0", "1": "1", "2": "2",
    "3": "3", "4": "4", "5": "5", "6": "6",
    "7": "7", "8": "8", "9": "9", "0": "0",
    "A": "2", "B": "2", "C": "2",
    "D": "3", "E": "3", "F": "3",
    "G": "4", "H": "4", "I": "4",
    "J": "5", "K": "5", "L": "5",
    "M": "6", "N": "6", "O": "6",
    "P": "7", "Q": "7", "R": "7", "S": "7",
    "T": "8", "U": "8", "V": "8",
    "W": "9", "X": "9", "Y": "9", "Z": "9",
    ",": "1", ".": "1", "?": "1", "!": "1",
}
for N in range(int(input())):
    s = input()
    for i in s:
        print(m.get(i, ""), end="")
    print()
