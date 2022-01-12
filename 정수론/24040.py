n = int(input())

for i in range(n):
    num = int(input())
    if (num % 9 == 0) or (num % 3 == 2):
        print("TAK")
        continue
    print("NIE")