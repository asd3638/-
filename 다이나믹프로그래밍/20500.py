# 이동하기
# 오/아/대 로만 이동이 가능 사탕의 개수를 최대로 선택
# dp[i][j] 면 넘어올 수 있는 가짓 수에 해당하는 dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1] 중에서 가장 큰 것을 선택
n, m = map(int, input().split())
s = []
dp = [[0] * (m + 1) for i in range(n + 1)]
for i in range(n):
    s.append(list(map(int, input().split())))
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = s[i - 1][j - 1] + max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
print(dp[n][m])


