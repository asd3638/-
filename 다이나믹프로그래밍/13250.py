n = int(input())
dp = [-1] * n

# 답은 맞게 나오는데 백준에서 틀림 결국 c++ 코드로 품
def f(x):
    if x >= n:
        return 0
    if dp[x] >= 0:
        return dp[x]
    ret = 0
    for count in range(1, 7):
        ret += round((1.00 / 6.00) * (1 + f(x + count)), 13)
    dp[x] = ret
    return dp[x]

print(f(0))