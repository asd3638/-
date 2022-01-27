
# 최적의 해를 도출해내는 그리디 전략을 생각해내는게 중요했던 문제

# 입력
n = int(input())
times = [list(map(int, input().split())) for _ in range(n)]
answer = 1
# 정렬
times.sort(key=lambda x: (x[1], x[0]))
right_index = times[0][1]

for i in range(1, len(times)):
    # 회의 시간이 겹치지 않을 때
    if times[i][0] >= right_index:
        answer += 1
        right_index = times[i][1]
print(answer)
