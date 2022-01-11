# 앞 선 k 배열이 정렬되어 있다고 가정한 채 k+1 이 들어갈 수 있는 위치에 삽입
# 앞 선 배열이 정렬됨을 가정한 알고리즘이기 때문에 선택 정렬과는 다르게 확정할 수 있는 break 문이 for 문 중간에 있다.
# 그래서 이미 어느정도 정렬된 경우라면 정렬 알고리즘 중 빠른 퀵 정렬보다도 빠를 수 있다.

array = [2, 3, 1, 4]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break

print(array)