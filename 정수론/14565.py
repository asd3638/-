import math

a, b = map(int, input().split())
x = 1
y = 0
print(a - b, end=' ')

def ex_gcd(a, b, x, y):
    if b == 0:
        x = 1
        y = 0
        return a
    ret = ex_gcd(b, a % b, x, y)
    temp = y
    y = x - (a / b) * y
    x = temp
    if x <= 0:
        x += b
        y -= a
    return ret

if math.gcd(a, b) != 1:
    x = -1
else:
    ex_gcd(a, b, x, y)
print(x)