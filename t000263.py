import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE t(ID INT, len INT, thi INT)")
conn.commit()
for n in range(int(input())):
    m = int(input())
    for i in range(m):
        s = [int(b) for b in input().split()]
        c.execute("INSERT INTO t VALUES (%d, %d, %d)" % (s[2], s[0], s[1]))
        conn.commit()
    cur = c.execute("SELECT id from t order by len desc, thi asc, id desc")
    for r in cur:
        print(r[0])
        break
    c.execute("DELETE from t")
    conn.commit()
conn.close()
