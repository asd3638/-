inp = int(input())

for i in range(inp):
    n = int(input())

    def rec(n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 4
        return rec(n - 3) + rec(n - 2) + rec(n - 1)

    print(rec(n))
