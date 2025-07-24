import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
board = data[2:N+2]

min_paint = float('inf')

for i in range(N - 7):
    for j in range(M - 7):
        w = 0
        b = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if board[k][l] == 'B':
                        w += 1
                    else:
                        b += 1
                else:
                    if board[k][l] == 'B':
                        b += 1
                    else:
                        w += 1
        min_paint = min(min_paint, w, b)

print(min_paint)