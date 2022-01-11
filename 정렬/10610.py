import sys
input = sys.stdin.readline

nums = [int(i) for i in list(input())[:-1]]

# 30 의 배수가 아닌 경우
if (0 not in nums) or (sum(nums) % 3 != 0):
    print(-1)
    exit()

print(''.join(str(e) for e in sorted(nums, reverse=True)))