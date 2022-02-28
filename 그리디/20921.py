n, k = map(int, input().split())

answer = [i for i in range(n, 0, -1)]
value = sum(answer[1:])

try:
    for i in range(n - 1, 0, -1):
        for j in range(n - 1, n - i - 1, -1):
            if value == k:
                raise NotImplementedError
            answer.insert(j - 1, answer.pop(j))
            value -= 1
    for i in answer:
        print(i, end=' ')
except:
    for i in answer:
        print(i, end=' ')
