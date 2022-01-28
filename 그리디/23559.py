# 입력
n, m = map(int, input().split())
meals = [list(map(int, input().split())) for _ in range(n)]
answer = 0
index = 1
# 정렬
meals.sort(key=lambda x: (x[1] - x[0]), reverse=True)

for meal in meals:
    # 굶지 않아야 하고 1000원 짜리보단 비싸야해
    needed = (1000 * (len(meals) - index))
    # print(needed)
    # print(meal)
    if (meal[1] < meal[0]) and (m >= (5000 + needed)):
        answer += meal[0]
        m -= 5000
        index += 1
        continue
    if m >= 1000:
        answer += meal[1]
        m -= 1000
        index += 1
        continue

print(answer)
