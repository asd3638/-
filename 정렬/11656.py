input_str = input()
answer = []
for i in range(len(input_str)):
    answer.append(input_str[i:])
for i in sorted(answer, key=lambda s: s[0]):
    print(i)