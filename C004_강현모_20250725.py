# C004 - 분해합 (백준)

n = int(input())

for i in range(n):
    num = i
    temp = i

    while temp > 0:
        num += temp % 10
        temp //= 10

    if num == n:
        n = 0
        print(i)
        break

if n != 0:
    print(0)