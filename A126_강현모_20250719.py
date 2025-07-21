import sys

input = sys.stdin.read

num = int(input().strip())

if num < 100:
    print(num)
else:
    count = 0
    for i in range(100, num + 1):
        a = i // 100
        b = (i // 10) % 10
        c = i % 10
        if (b - a) == (c - b):
            count += 1
    print(99 + count)