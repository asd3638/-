import sys
input = sys.stdin.readline

n = int(input())
in_list = [0] * 2000001
checked = [0] * 2000001

for i in list(map(int, input().split())):
    in_list[i] += 1

# 예외 조건
for i in range(0, 2):
    if in_list[i] == 0:
        print(i)
        sys.exit(0)

for i in range(1, 2000001):
    if in_list[i] == 0:
        continue
    for j in range(1, 2000001):
        if i * j >= 2000001:
            break
        if in_list[j] == 0:
            continue
        checked[i * j] = 1

for i in range(2, 2000001):
    if checked[i] == 1:
        continue
    print(i)
    sys.exit(0)
