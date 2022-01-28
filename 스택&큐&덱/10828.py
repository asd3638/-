n = int(input())
stack = []
for i in range(n):
    s = input()
    if s[:4] == "push":
        stack.append(s.split()[1])
    elif s == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif s == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack) - 1])
    elif s == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif s == "size":
        print(len(stack))
