n, k = map(int, input().split())

answer = [i for i in range(1, n + 1)]
print(answer.pop(k), end=' ')
for i in answer:
    print(i, end=' ')
