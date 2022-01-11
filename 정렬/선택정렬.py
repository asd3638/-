# n n-1 n-2 씩 제일 작은 숫자 찾아서 제일 앞으로 이동

array = [2, 3, 1, 4]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)