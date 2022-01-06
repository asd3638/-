from collections import deque
n = int(input())

for i in range(n):
    q = deque()
    answer = "YES"
    for j in input():
        if j == "(":
            q.append("(")
            continue
        if len(q) > 0:
            q.pop()
        else:
            answer = "NO"
            break
    if len(q) > 0:
        answer = "NO"
    print(answer)
