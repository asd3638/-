from itertools import combinations

n = int(input())

for _ in range(n):
    k = int(input())
    words = [input() for _ in range(k)]
    combination = list(combinations(words, 2))
    for a, b in combination:
        tmp_a = a + b
        tmp_b = b + a
        if tmp_a == tmp_a[::-1]:
            print(tmp_a)
            break
        if tmp_b == tmp_b[::-1]:
            print(tmp_b)
            break
    else:
        print(0)
