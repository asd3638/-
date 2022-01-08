import math

n = int(input())
x = list(map(int, input().split()))

min_value = 0
max_value = 0
if len(x) == 1:
    print("권병장님, 중대장님이 찾으십니다")
else:
    y = list(map(int, input().split()))
    min_value = min([x[i] - y[i] for i in range(len(x) - 1)])
    max_value = max([x[i] + y[i] for i in range(len(x) - 1)])

    print(min_value)
    print(max_value)
    if (x[-1] >= min_value) and (x[-1] <= max_value):
        print("권병장님, 중대장님이 찾으십니다")
    else:
        print("엄마 나 전역 늦어질 것 같아")

