n = int(input())
dp = [False] * 1010
dp[1] = True
dp[2] = False
dp[3] = True
dp[4] = False

if n > 3:
    for i in range(4, n + 1):
        if not dp[i - 1]:
            dp[i] = True
            continue
        if not dp[i - 3]:
            dp[i] = True
            continue
        dp[i] = False

if dp[n]:
    print("SK")
else:
    print("CY")


