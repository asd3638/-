# 모든 원소의 값이 0보다 크거나 같다고 가정 (인덱스를 값으로 사용하기 때문에 어쩔 수 없음)
# 0 100
array = [2, 3, 1, 4]
# 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')