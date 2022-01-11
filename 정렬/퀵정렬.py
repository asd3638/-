# 정렬 배열은 어떠한 기준값에 대해 왼쪽은 작고 오른쪽은 큰 특징을 가지고 있음을 이용함
# 왼쪽 영역과 오른쪽 영역으로 영역을 분할해 정렬한다.

array = [2, 3, 1, 4]

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [i for i in tail if i <= pivot]
    right_side = [i for i in tail if i > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
