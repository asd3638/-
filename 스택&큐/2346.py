from collections import deque

n = int(input())
q = deque(enumerate(map(int, input().split())))
index = 0
answer = []

while q:
    if index == 0:
        tmp = q.popleft()
        answer.append(tmp[0] + 1)
        if tmp[1] > 0:
            index = tmp[1] - 1
        else:
            index = tmp[1]
        continue
    if index > 0:
        q.append(q.popleft())
        index -= 1
    else:
        q.appendleft(q.pop())
        index += 1
for r in answer:
    print(r, end=' ')




