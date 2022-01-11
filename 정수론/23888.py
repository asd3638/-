import math

a, d = map(int, input().split())
pre = [0]
pre.append(a)
g = math.gcd(a, d)

for i in range(2, 1010101):
    pre.append(pre[i - 1] + a + (i -1) * d)
for i in range(int(input())):
    k, b, c = map(int, input().split())
    if k == 1:
        print(pre[c] - pre[b - 1])
        continue
    if b == c:
        print(pre[b] - pre[b - 1])
        continue
    else:
        print(g)

