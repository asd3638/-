n = int(input())

a_list = sorted(list(map(int, input().split())))
b_list = sorted(list(map(int, input().split())), reverse=True)

print(sum([a_list[i] * b_list[i] for i in range(len(a_list))]))
