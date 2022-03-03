# 민균이의 계략
# 배열의 수 중 상승하는 수의 최대 개수

# 예외
# 8
# 1 2 3 100 4 101 5 6

n = int(input())
s = list(map(int, input().split()))
dp = []
answer = 0

for i in range(n):
    tmp_max = 1
    for j in range(len(dp)):
        if i == 0:
            break
        if s[i] > dp[j][0]:
            if tmp_max < dp[j][1] + 1:
                # 여기서 dp[j][0] 을 update 하면 안된다 !
                tmp_max = dp[j][1] + 1
    tmp = [s[i], tmp_max]
    dp.append(tmp)

for i in dp:
    if i[1] > answer:
        answer = i[1]
print(dp)
print(answer)



