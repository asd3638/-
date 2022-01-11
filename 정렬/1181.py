import sys

N = int(sys.stdin.readline())
table = list(set([sys.stdin.readline().strip() for _ in range(N)]))

table.sort(key=lambda x: (len(x), x))
for _ in table:
    print(_)
