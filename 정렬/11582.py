import math
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
answer = []
k = int(input())
i = 0

for _ in range(k):
    for j in sorted(nums[i:i + (n // k)]):
        answer.append(j)
    i += (n // k)

print(*answer)