import math

n = int(input())
alice = [int(i) for i in input().split()]
bob = [int(i) for i in input().split()]

answer = -10e9
for i in alice:
    a = 10e9
    for j in bob:
        a = min(a, abs(i - j))
    answer = max(answer, a)
print(answer)
