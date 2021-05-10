mm = {"A": "UNIQUE", "A#": "Bb", "B": "UNIQUE",
      "C": "UNIQUE", "Bb": "A#", "C#": "Db",
      "Db": "C#", "D": "UNIQUE", "D#": "Eb",
      "Eb": "D#", "E": "UNIQUE", "F": "UNIQUE",
      "F#": "Gb", "Gb": "F#", "G": "UNIQUE",
      "G#": "Ab", "Ab": "G#"}
try:
    n = 0
    while 1:
        n = n + 1
        s = input().split()
        if mm[s[0]] == "UNIQUE":
            print("Case %d: UNIQUE" % n)
        else:
            print("Case %d: %s %s" % (n, mm[s[0]], s[1]))
except EOFError:
    pass
